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
from common.utils import global_log_append, get_mime_type

from tenacity import retry, wait_fixed, stop_after_attempt


class CommerceAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.initData()

    def initData(self):
        asyncio.run(self.set_client_secret_sign())
        asyncio.run(self.set_token())

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
            print("토큰 획득 성공")
            data = json.loads(str(res.text))
            self.token = data["access_token"]
            self.expires_in = data["expires_in"]  # 남은 유효 시간
            self.token_type = data["token_type"]
            await asyncio.sleep(1)
        else:
            global_log_append("토큰 획득 실패")
            print("토큰 획득 실패")

    def get_headers(self):
        # 유효 시간이 지난 테스트용 토큰
        # self.token = "2DtQ2IW1TX2ZLuMD6Qkesw=="
        return {"Authorization": f"Bearer {self.token}", "content-type": "application/json"}

    def get_headers_multipart(self):
        # 유효 시간이 지난 테스트용 토큰
        # self.token = "2DtQ2IW1TX2ZLuMD6Qkesw=="
        return {"Authorization": f"Bearer {self.token}"}

    async def set_client_secret_sign(self):
        self.timestamp = self.get_timestamp()
        # 밑줄로 연결하여 password 생성
        password = self.client_id + "_" + str(self.timestamp)
        # bcrypt 해싱
        hashed = bcrypt.hashpw(password.encode("utf-8"), self.client_secret.encode("utf-8"))
        # base64 인코딩
        self.client_secret_sign = pybase64.standard_b64encode(hashed).decode("utf-8")
        await asyncio.sleep(1)

    # 상품 업로드
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def add_product(self, originProduct: dict):
        headers = self.get_headers()
        api_url = "https://api.commerce.naver.com/external/v2/products"
        result = False

        result = requests.post(api_url, headers=headers, json=originProduct)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        # 성공한 경우 200
        if result.status_code == HTTPStatus.OK:
            print("성공")
            result = True
            fail_reason = ""

        # 입력한 값이 유효하지 않을 경우 400
        elif result.status_code == HTTPStatus.BAD_REQUEST:
            print("실패")
            fail_reason = result_json["invalidInputs"][0]
            global_log_append(result_json)

        # 토큰이 유효하지 않을 경우 401
        elif result.status_code == HTTPStatus.UNAUTHORIZED:
            print("실패")
            fail_reason = result_json
            global_log_append(fail_reason)
            self.initData()
            raise Exception(result_json)

        # 그 외의 경우
        else:
            result = False
            fail_reason = result_json
            print("실패")

        return result, fail_reason

    # 이미지 업로드
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def multi_image_upload(self, img_list: list):
        print("multi_image_upload")

        uploaded_images = []

        if len(img_list) > 10:
            print("이미지수", len(img_list))
            print("이미지는 최대 10개까지만 등록가능합니다.")
            return uploaded_images

        if len(img_list) <= 0:
            print("입력된 이미지가 없습니다.")
            return uploaded_images

        api_url = f"https://api.commerce.naver.com/external/v1/product-images/upload"

        files = {}

        for i in range(len(img_list)):
            img_path = img_list[i]
            img_name = os.path.basename(img_path)
            img_type = get_mime_type(img_path)
            img_binary = open(img_path, "rb").read()
            files.update({f"imageFiles[{i}]": (f"{img_name}", img_binary, img_type)})

        headers = self.get_headers_multipart()
        res = requests.post(api_url, headers=headers, files=files)

        result_text = res.text
        res_json = json.loads(result_text)
        uploaded_images = res_json["images"]

        uploaded_images = [x["url"] for x in uploaded_images]
        print(uploaded_images)

        await asyncio.sleep(1)

        return uploaded_images

    # 상품번호 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def get_product(self, channelProductNo):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v2/products/channel-products/{channelProductNo}"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 모든 카테고리 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def get_all_category(self):
        headers = self.get_headers()
        api_url = "https://api.commerce.naver.com/external/v1/categories"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 상품명 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    async def get_all_product_from_keyword(self, keyword: str):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v1/product-models?name={keyword}&page=1&size=100"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        await asyncio.sleep(1)
        return result_json

    # 상품 id 단일 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def get_product_from_id(self, id):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v1/product-models/{id}"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 주소록 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def search_addr(self):
        headers = self.get_headers()
        api_url = "https://api.commerce.naver.com/external/v1/seller/addressbooks-for-page?page=1"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 묶음배송그룹 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def delivery_bundle_group(self):
        headers = self.get_headers()
        api_url = "https://api.commerce.naver.com/external/v1/product-delivery-info/bundle-groups?base_group=true"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 전체 속성값 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def get_product_attribute_value_units(self):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v1/product-attributes/attribute-value-units"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 카테고리별 속성값 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def get_product_attribute_values_from_category_id(self, category_id):
        headers = self.get_headers()
        api_url = (
            f"https://api.commerce.naver.com/external/v1/product-attributes/attribute-values?categoryId={category_id}"
        )

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json

    # 카테고리별 속성 조회
    @retry(
        wait=wait_fixed(3),  # 3초 대기
        stop=stop_after_attempt(2),  # 2번 재시도
    )
    def get_product_attributes_from_category_id(self, category_id):
        headers = self.get_headers()
        api_url = f"https://api.commerce.naver.com/external/v1/product-attributes/attributes?categoryId={category_id}"

        result = requests.get(api_url, headers=headers)
        result_text = result.text.encode("utf-8")
        result_json = json.loads(result_text)
        print(f"status_code: {result.status_code}")
        print(result_json)

        if result.status_code == HTTPStatus.OK:
            print("성공")
        else:
            print("실패")
            global_log_append(result_json)
            self.initData()
            raise Exception(result_json)

        return result_json


if __name__ == "__main__":

    # API
    client_id = "1yhn7qj8fvbQYerxmGO8ja"
    client_secret = "$2a$04$3iOzPhDU7KJN247s6UTSCO"

    product_id = 7984456905

    # 50002627 -> 스포츠/레저>등산>등산의류>재킷
    # 50002326 -> 디지털/가전>음향가전>마이크>일반마이크
    # 50000091 -> 노트북 악세사리
    category_id = 50000091

    searchBot = CommerceAPI(client_id=client_id, client_secret=client_secret)

    data = ""

    # 상품 조회
    # data = searchBot.get_product(product_id)

    # 모든 카테고리 조회
    # data = searchBot.get_all_category()

    # 상품명 조회
    # data = asyncio.run(searchBot.get_all_product_from_keyword("햇반"))

    # 상품 단일 조회
    # data = searchBot.get_product_from_id(5825766254)

    # 주소록 조회
    # data = searchBot.search_addr()

    # 묶음배송그룹 조회
    # data = searchBot.delivery_bundle_group()

    # 전체 속성값 조회
    # data = searchBot.get_product_attribute_value_units()

    # 카테고리별 속성값 조회
    # data = searchBot.get_product_attribute_values_from_category_id(category_id)

    # 카테고리별 속성 조회
    data = searchBot.get_product_attributes_from_category_id(category_id)

    print(type(data))

    print(data)

    print(len(data))

    # clipboard.copy(str(data))

    # 유효시간 지난 토큰 테스트
    # {"access_token":"2DtQ2IW1TX2ZLuMD6Qkesw==","expires_in":8295,"token_type":"Bearer"}
