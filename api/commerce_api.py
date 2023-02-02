#!/usr/bin/env python
if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from http import HTTPStatus
import bcrypt
import pybase64
import http.client
import requests
import json
import time
import asyncio
from common.utils import global_log_append
import clipboard


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

    # 상품 조회
    searchBot = CommerceAPI(client_id=client_id, client_secret=client_secret)

    data = searchBot.get_product(product_test)

    print(data)

    clipboard.copy(str(data))
