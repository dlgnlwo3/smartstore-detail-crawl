import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from api.commerce_api import CommerceAPI
import asyncio


def get_catalog_from_product_name(product_name: str, cmBot: CommerceAPI):

    catalog_info = ""

    try:
        data = get_data(product_name, cmBot)

        search_reseult_list = data["contents"]

        for i, search_reseult in enumerate(search_reseult_list):
            print(f"{i}, {search_reseult}")

            # 카탈로그 검색결과에서 0번째 결과를 가져옴
            catalog_info = search_reseult
            break

            # # 카탈로그 이름과 상품명이 일치하는 경우 실행
            # if search_reseult["name"] == product_name:
            #     catalog_info = search_reseult
            #     break

    except Exception as e:
        catalog_info = ""
        print(f"{product_name} 검색 결과가 없습니다.")

    return catalog_info


def get_data(product_name: str, cmBot: CommerceAPI):

    data = asyncio.run(cmBot.get_all_product_from_keyword(product_name))
    return data


if __name__ == "__main__":

    print()
