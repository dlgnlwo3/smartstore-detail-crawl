import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#!/usr/bin/env python
from http import HTTPStatus
import bcrypt
import pybase64
import http.client
import requests
import json
import time
import os
from common.utils import get_mime_type
import asyncio
from api.naver_shop import NaverShopAPI


class CommerceCategory:
    def __init__(self, client_id, client_secret, account_id=""):

        self.main_url = f"https://api.commerce.naver.com"
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_id = account_id
        self.initData()

    def initData(self):
        asyncio.run(self.set_client_secret_sign())
        asyncio.run(self.set_token())

    # 전자서명 (self.timestamp, self.client_secret_sign)
    async def set_client_secret_sign(self):

        self.timestamp = round(time.time() * 1000)

        # 밑줄로 연결하여 password 생성
        password = self.client_id + "_" + str(self.timestamp)

        # bcrypt 해싱
        hashed = bcrypt.hashpw(password.encode("utf-8"), self.client_secret.encode("utf-8"))

        # base64 인코딩 -> param으로 사용될 것
        self.client_secret_sign = pybase64.standard_b64encode(hashed).decode("utf-8")

    # 토큰 (self.token)
    async def set_token(self):
        auth_url = "https://api.commerce.naver.com/external/v1/oauth2/token"
        params = {
            "client_id": self.client_id,  # 제공된 클라이언트 ID
            "timestamp": self.timestamp,  # 전자서명 생성 시 사용된 밀리초(millisecond) 단위의 Unix 시간. 5분간 유효
            "client_secret_sign": self.client_secret_sign,  # 전자서명
            "grant_type": "client_credentials",  # OAuth2 인증 방식 -> client_credentials 고정
            "type": "SELF",
            "account_id": self.account_id,  # type이 SELLER인 경우 입력해야 하는 판매자 ID
        }
        res = requests.post(auth_url, params=params)
        if res.status_code == HTTPStatus.OK:
            data = json.loads(str(res.text))
            self.token = data["access_token"]
        else:
            print("토큰 가져오기 실패")

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}", "content-type": "application/json"}

    def get_all_category(self):
        api_url = "https://api.commerce.naver.com/external/v1/categories"
        headers = self.get_headers()
        upload_result = requests.get(api_url, headers=headers)
        result_text = upload_result.text.encode("utf-8")
        res_json = json.loads(result_text)
        return res_json

    def get_category_by_product_name(self, product_name: str):
        api_url = f"https://api.commerce.naver.com/external/v1/product-images/upload"
        files = {}
        headers = self.get_headers()
        upload_result = requests.post(api_url, headers=headers, files=files)

        result_text = upload_result.text
        res_json = json.loads(result_text)
        uploaded_images = res_json["images"]
        return uploaded_images

    def get_category_id_by_product_name(self, product_name: str, all_categories: dict):

        category_id = ""

        naverBot = NaverShopAPI()
        items = naverBot.fetch_sync_items(product_name)
        first_competitor_category_name = ""
        if len(items) == 0:
            return ""

        first_competitor_item = items[0]

        # 경쟁사 카테고리 조회
        category1 = first_competitor_item["category1"]
        category2 = first_competitor_item["category2"]
        category3 = first_competitor_item["category3"]
        category4 = first_competitor_item["category4"]

        if category1:
            first_competitor_category_name += category1
        if category2:
            first_competitor_category_name += f">{category2}"
        if category3:
            first_competitor_category_name += f">{category3}"
        if category4:
            first_competitor_category_name += f">{category4}"

        for category in all_categories:
            if first_competitor_category_name == category["wholeCategoryName"]:
                category_id = category["id"]
                break

        return category_id


if __name__ == "__main__":

    # 콘솔워크 키정보
    client_id = "1yhn7qj8fvbQYerxmGO8ja"  # 제공된 클라이언트 ID
    client_secret = "$2a$04$3iOzPhDU7KJN247s6UTSCO"  # API키

    cmBot = CommerceCategory(client_id, client_secret)
    cmBot.get_all_category()
