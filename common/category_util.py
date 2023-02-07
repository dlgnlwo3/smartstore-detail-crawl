import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from api.commerce_api import CommerceAPI


def get_category_id_from_product_name(product_name: str, cmBot: CommerceAPI):

    category_id = ""

    # 상품명 조회
    data = cmBot.get_all_product_from_keyword(product_name)

    # 조회 결과가 없을 경우
    if data["totalElements"] <= 0:
        print(f"{product_name} 검색 결과가 없습니다.")
        return category_id

    category_id = data["contents"][0]["categoryId"]

    return category_id


if __name__ == "__main__":

    print()
