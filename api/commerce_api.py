#!/usr/bin/env python
if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from http import HTTPStatus
import bcrypt
import pybase64
import requests
import json
import time
import asyncio
from common.utils import global_log_append


class CommerceAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.initData()

    def initData(self):
        asyncio.run(self.set_client_secret_sign())
        asyncio.run(self.set_token())
        # self.set_client_secret_sign()
        # self.set_token()

    def get_timestamp(self):
        return round(time.time() * 1000)

    async def set_token(self):
        auth_url = "https://api.commerce.naver.com/external/v1/oauth2/token"
        params = {
            "client_id": self.client_id,
            "timestamp": self.timestamp,
            "client_secret_sign": self.client_secret_sign,
            "grant_type": "client_credentials",
            "type": "SELF",
        }

        print(params)

        res = requests.post(auth_url, params=params)
        print(res.text)

        if res.status_code == HTTPStatus.OK:
            print("토큰가져오기 성공")
            data = json.loads(str(res.text))
            self.token = data["access_token"]
            await asyncio.sleep(1)
        else:
            global_log_append("토큰 가져오기 실패")
            print("토큰 가져오기 실패")

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}", "content-type": "application/json"}

    def search(self):
        print("search")

    async def set_client_secret_sign(self):

        self.timestamp = self.get_timestamp()
        # 밑줄로 연결하여 password 생성
        password = self.client_id + "_" + str(self.timestamp)
        # bcrypt 해싱
        hashed = bcrypt.hashpw(password.encode("utf-8"), self.client_secret.encode("utf-8"))
        # base64 인코딩
        self.client_secret_sign = pybase64.standard_b64encode(hashed).decode("utf-8")

        await asyncio.sleep(1)

    # 상품번호 조회
    def get_product(self, channelProductNo):
        import http.client

        conn = http.client.HTTPSConnection("api.commerce.naver.com")
        headers = self.get_headers()

        conn.request("GET", f"/external/v2/products/channel-products/{channelProductNo}", headers=headers)

        res = conn.getresponse()
        res_data = res.read()
        txt = res_data.decode("utf-8")
        data = json.loads(txt)
        return data

    # 모든 카테고리 조회
    def get_all_category(self):
        api_url = "https://api.commerce.naver.com/external/v1/categories"
        headers = self.get_headers()
        upload_result = requests.get(api_url, headers=headers)
        result_text = upload_result.text.encode("utf-8")
        res_json = json.loads(result_text)
        return res_json

    # 상품명 조회
    def get_all_product_from_keyword(self, keyword: str):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v1/product-models?name={keyword}&page=1&size=100"
        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        res_json = json.loads(result_text)
        return res_json

    # 상품 id 단일 조회
    def get_product_from_id(self, id):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v1/product-models/{id}"
        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        res_json = json.loads(result_text)
        return res_json

    # 주소록 조회
    def search_addr(self):
        headers = self.get_headers()
        api_url = "https://api.commerce.naver.com/external/v1/seller/addressbooks-for-page?page=1"
        upload_result = requests.get(api_url, headers=headers)
        result_text = upload_result.text
        res_json = json.loads(result_text)
        addressBooks = res_json["addressBooks"]

        print("==주소록==")
        for addr in addressBooks:
            if str(addr["name"]).find("빅스타") > -1:
                print(addr)
                # print(addr["addressBookNo"], addr["name"])
        print()

        return addressBooks

    # 묶음배송그룹 조회
    def delivery_bundle_group(self):
        headers = self.get_headers()
        api_url = "https://api.commerce.naver.com/external/v1/product-delivery-info/bundle-groups?base_group=true"
        upload_result = requests.get(api_url, headers=headers)
        result_text = upload_result.text
        res_json = json.loads(result_text)

        print("==묶음배송그룹==")
        bundle_groups = res_json["contents"]
        for group in bundle_groups:
            print(group["id"], group["name"])

        return bundle_groups

    # 상품 업로드
    def add_product(self, originProduct: dict):
        print("product_add")
        result = False
        api_url = "https://api.commerce.naver.com/external/v2/products"
        headers = self.get_headers()
        res = requests.post(api_url, headers=headers, json=originProduct)
        print("상품등록결과")

        if res.status_code == HTTPStatus.OK:
            print("등록 성공")
            result = True
            fail_reason = ""
        else:
            print(res.text)
            res_json = json.loads(res.text)
            res_json = res_json["invalidInputs"][0]
            print("등록 실패")
            global_log_append("[등록 실패]")
            global_log_append(res_json)
            fail_reason = f"{res_json['name']} {res_json['message']}"

        return result, fail_reason


if __name__ == "__main__":

    # API
    client_id = "1yhn7qj8fvbQYerxmGO8ja"
    client_secret = "$2a$04$3iOzPhDU7KJN247s6UTSCO"

    product_test = 7984456905

    searchBot = CommerceAPI(client_id=client_id, client_secret=client_secret)

    # 상품 조회
    # data = searchBot.get_product(product_test)

    # 모든 카테고리 조회
    # data = searchBot.get_all_category()

    # 주소록 조회
    # data = searchBot.search_addr()

    # 묶음배송그룹 조회
    # data = searchBot.delivery_bundle_group()

    # 상품명 조회
    # data = searchBot.get_all_product_from_keyword("햇반")

    # 상품 단일 조회
    data = searchBot.get_product_from_id(5825766254)

    print(type(data))

    print(data)

    print(len(data))

    # clipboard.copy(str(data))
