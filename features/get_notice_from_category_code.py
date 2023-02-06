if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2

from common.utils import global_log_append
from common.category_file import CategoryFile
from enums.product_info_provided_notice_enum import ProductInfoProvidedNotice
from config import *

from api.commerce_api import CommerceAPI


class CategoryCodeConverter:
    def __init__(self, category_code, all_categories):
        self.category_code = category_code
        self.all_categories = all_categories
        print(f"카테고리코드: {self.category_code}")

    def get_notice(self):

        notice = ProductInfoProvidedNotice.ETC.value

        try:
            category_dict = next((item for item in self.all_categories if item["id"] == self.category_code), None)

            category_name: str = category_dict["wholeCategoryName"]

            large_category = category_name.split(">")[0]

            print(large_category)

            print(f"{self.category_code}, {large_category}")

            if large_category == "가구/인테리어":
                notice = ProductInfoProvidedNotice.FURNITURE.value
            elif large_category == "도서":
                notice = ProductInfoProvidedNotice.BOOKS.value
            elif large_category == "디지털/가전":
                notice = ProductInfoProvidedNotice.HOME_APPLIANCES.value
            elif large_category == "생활/건강":
                notice = ProductInfoProvidedNotice.DIGITAL_CONTENTS.value
            elif large_category == "스포츠/레저":
                notice = ProductInfoProvidedNotice.SPORTS_EQUIPMENT.value
            elif large_category == "식품":
                notice = ProductInfoProvidedNotice.FOOD.value
            elif large_category == "여가/생활편의":
                notice = ProductInfoProvidedNotice.ETC.value
            elif large_category == "출산/육아":
                notice = ProductInfoProvidedNotice.KIDS.value
            elif large_category == "패션의류":
                notice = ProductInfoProvidedNotice.WEAR.value
            elif large_category == "패션잡화":
                notice = ProductInfoProvidedNotice.FASHION_ITEMS.value
            elif large_category == "화장품/미용":
                notice = ProductInfoProvidedNotice.COSMETIC.value
        except Exception as e:
            print("카테고리 오류")

        return notice


if __name__ == "__main__":

    client_id = "1yhn7qj8fvbQYerxmGO8ja"
    client_secret = "$2a$04$3iOzPhDU7KJN247s6UTSCO"

    Bot = CommerceAPI(client_id=client_id, client_secret=client_secret)

    all_categories = Bot.get_all_category()

    category_code = "50012420"
    print(category_code)

    # 조건에 맞는 첫번째 dict가 검색됩니다.
    category_dict = next((item for item in all_categories if item["id"] == category_code), None)

    category_name: str = category_dict["wholeCategoryName"]

    category_name = category_name.split(">")[0]

    print(category_name)

    print()

    # excel_file = r"D:\Consolework\smartstore-detail-crawl\smartstore\스마트스토어_카테고리코드.xls"
    # category_code = "50012420"

    # if os.path.isfile(excel_file):
    #     print(f"{excel_file}")
    #     category_file = CategoryFile(excel_file)
    #     df_category = category_file.df_category
    #     # print(df_category)

    #     category_data = df_category[(df_category["카테고리번호"] == category_code)].iloc[0]
    #     category_code = category_data["카테고리번호"]
    #     large_category = category_data["대분류"]
    #     medium_category = category_data["중분류"]
    #     small_category = category_data["소분류"]
    #     detail_category = category_data["세분류"]
    #     print(f"{category_code}, {large_category}, {medium_category}, {small_category}, {detail_category}")

    # else:
    #     print(f"카테고리 파일 오류")
