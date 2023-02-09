import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from api.commerce_api import CommerceAPI
import asyncio


def get_category_id_from_product_name(product_name: str, cmBot: CommerceAPI):

    category_id = ""

    data = get_data(product_name, cmBot)

    while data["totalElements"] == 0:

        if data["totalElements"] == 0:
            product_name = product_name[: product_name.rfind(" ")]
            print(product_name)
            data = get_data(product_name, cmBot)
            print(data)

        if product_name.rfind(" ") <= -1:
            print(product_name)
            break

    try:
        category_id = data["contents"][0]["categoryId"]
    except Exception as e:
        category_id = ""
        print(f"{product_name} 검색 결과가 없습니다.")

    return category_id


def get_data(product_name: str, cmBot: CommerceAPI):

    data = asyncio.run(cmBot.get_all_product_from_keyword(product_name))
    return data


if __name__ == "__main__":

    print()
