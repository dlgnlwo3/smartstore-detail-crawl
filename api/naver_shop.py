# 네이버 검색 API 예제 - 블로그 검색
import json
import urllib.request
import os
import urllib
import asyncio
from timeit import default_timer as timer
from datetime import timedelta
from urllib.request import Request, urlopen
import pandas as pd

## 한번에 10개까지 요청가능
class NaverShopAPI:
    def __init__(self):
        self.account = [
            {"CLIENT_ID": "G18H9N2YEDZHfGa0ddXt", "CLIENT_SECRET": "gRuXVfYR8w", "COMPANY": "김범관"},
        ]
        self.account_i = 0

    def setKeys(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def initData(self):
        self.CLIENT_ID = "G18H9N2YEDZHfGa0ddXt"
        self.CLIENT_SECRET = "gRuXVfYR8w"

    def fetch_sync_total_count(self, keyword):
        total_count = None
        ENCTEXT = urllib.parse.quote(keyword)
        url = "https://openapi.naver.com/v1/search/shop?display=100&query=" + ENCTEXT  # JSON 결과
        request = Request(url)
        request.add_header("X-Naver-Client-Id", self.account[self.account_i]["CLIENT_ID"])
        request.add_header("X-Naver-Client-Secret", self.account[self.account_i]["CLIENT_SECRET"])
        response = urlopen(request)
        rescode = response.getcode()
        response_body = response.read()
        if rescode == 200:
            response_dict = json.loads(response_body.decode("utf-8"))
            print(response_dict)
            total_count = response_dict["total"]
        return total_count

    def fetch_sync_items(self, keyword):
        items = None
        ENCTEXT = urllib.parse.quote(keyword)
        url = "https://openapi.naver.com/v1/search/shop?display=100&query=" + ENCTEXT  # JSON 결과
        request = Request(url)
        request.add_header("X-Naver-Client-Id", self.account[self.account_i]["CLIENT_ID"])
        request.add_header("X-Naver-Client-Secret", self.account[self.account_i]["CLIENT_SECRET"])
        response = urlopen(request)
        rescode = response.getcode()
        response_body = response.read()
        if rescode == 200:
            response_dict = json.loads(response_body.decode("utf-8"))
            items = response_dict["items"]
        return items

    async def fetch_total(self, keyword, loop):
        total_count = None
        ENCTEXT = urllib.parse.quote(keyword)
        url = "https://openapi.naver.com/v1/search/shop?display=100&query=" + ENCTEXT  # JSON 결과
        request = Request(url)
        request.add_header("X-Naver-Client-Id", self.account[self.account_i]["CLIENT_ID"])
        request.add_header("X-Naver-Client-Secret", self.account[self.account_i]["CLIENT_SECRET"])

        response = await loop.run_in_executor(None, urlopen, request)
        rescode = await loop.run_in_executor(None, response.getcode)
        response_body = await loop.run_in_executor(None, response.read)

        if rescode == 200:
            response_dict = json.loads(response_body.decode("utf-8"))
            total_count = response_dict["total"]
        return total_count

    async def search(self, keywords, loop):
        futures = [asyncio.ensure_future(self.fetch(keyword, loop)) for keyword in keywords]
        # 태스크(퓨처) 객체를 리스트로 만듦
        result = await asyncio.gather(*futures)  # 결과를 한꺼번에 가져옴
        return result


if __name__ == "__main__":

    keyword = "커클랜드 시그니춰 통후추 399g"
    start_time = timer()
    naverBot = NaverShopAPI()
    items = naverBot.fetch_sync_items(keyword)
    print(type(items))
    print(items)
    # df_items = pd.DataFrame.from_dict(items)
    # df_items.to_excel(f"하기스.xlsx")

    # # 한번에 10까지만 조회가능
    # keywords = ["여성 유니화", "편한힐", "면접구두", "승무원구두", "발편한구두", "여성 유니화", "편한힐", "면접구두", "편한힐", "면접구두"]
    # loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
    # loop.run_until_complete(naverBot.search(keywords, loop))  # main이 끝날 때까지 기다림
    # loop.close()  # 이벤트 루프를 닫음
