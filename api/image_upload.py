import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from http import HTTPStatus
import bcrypt
import pybase64
import requests
import json
import os
from common.utils import get_mime_type
import time
import asyncio
from common.utils import global_log_append


class CommerceImageUploader:
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
        await asyncio.sleep(1)

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
            await asyncio.sleep(1)
        else:
            global_log_append("토큰 가져오기 실패")
            print("토큰 가져오기 실패")

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}", "content-type": "application/json"}

    def get_headers_multipart(self):
        return {"Authorization": f"Bearer {self.token}"}

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

    # Request의 Content-type은 multipart/form-data이어야 합니다.
    # Content-type으로 boundary 구분자를 지정해야 합니다.
    # 각 파일 바이너리간에 boundary 구분자를 포함해주셔야 합니다.
    # 테스트
    def img_test(self):
        print("img_test")

        path = "/external/v1/product-images/upload"
        api_url = "https://api.commerce.naver.com{0}".format(path)

        # for i in range(len(image_list) + 1):

        #     img = image_list[i]

        img_path1 = r"C:\Users\bk\Pictures\Screenshots\스크린샷(1).png"
        img_path2 = r"C:\Users\bk\Pictures\Screenshots\sc.png"

        image_binary_1 = open(img_path1, "rb").read()
        image_binary_2 = open(img_path2, "rb").read()

        image_binary_1_type = get_mime_type(img_path1)
        image_binary_2_type = get_mime_type(img_path2)

        files = {
            "imageFiles[0]": ("sample_image_1.png", image_binary_1, image_binary_1_type),
            "imageFiles[1]": ("sample_image_2.png", image_binary_2, image_binary_2_type),
        }

        # files = {"imageFiles": ("test.png", image_binary, "image/png")}

        headers = self.get_headers_multipart()
        upload_result = requests.post(api_url, headers=headers, files=files)


if __name__ == "__main__":

    # parameter
    # 키정보
    client_id = ""
    client_secret = ""

    cmBot = CommerceImageUploader(client_id, client_secret)

    img_list = [
        r"D:\Consolework\smartstore-product-add\media\9788927449331.jpg",
        r"D:\Consolework\smartstore-product-add\media\9788934961871.jpg",
    ]
    cmBot.multi_image_upload(img_list)
