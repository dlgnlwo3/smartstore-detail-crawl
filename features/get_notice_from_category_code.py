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


class CategoryCodeConverter:
    def __init__(self, category_code):
        self.category_code = category_code
        print(f"카테고리코드: {self.category_code}")
        print(f"SMARTSTORE_CATEGORY_FILE: {SMARTSTORE_CATEGORY_FILE}")

    def get_notice(self):

        if os.path.isfile(SMARTSTORE_CATEGORY_FILE):
            category_file = CategoryFile(SMARTSTORE_CATEGORY_FILE)
            df_category = category_file.df_category
            category_data = df_category[(df_category["카테고리번호"] == self.category_code)].iloc[0]
            category_code = category_data["카테고리번호"]
            large_category = category_data["대분류"]
            medium_category = category_data["중분류"]
            small_category = category_data["소분류"]
            detail_category = category_data["세분류"]
            print(f"{category_code}, {large_category}, {medium_category}, {small_category}, {detail_category}")

            notice = ProductInfoProvidedNotice.ETC.value

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

        else:
            print(f"카테고리 파일 오류 -> 기타 공지사항으로 대체합니다.")
            notice = ProductInfoProvidedNotice.ETC.value

        return notice


if __name__ == "__main__":
    excel_file = r"D:\Consolework\smartstore-detail-crawl\smartstore\스마트스토어_카테고리코드.xls"
    category_code = "50012420"

    if os.path.isfile(excel_file):
        print(f"{excel_file}")
        category_file = CategoryFile(excel_file)
        df_category = category_file.df_category
        # print(df_category)

        category_data = df_category[(df_category["카테고리번호"] == category_code)].iloc[0]
        category_code = category_data["카테고리번호"]
        large_category = category_data["대분류"]
        medium_category = category_data["중분류"]
        small_category = category_data["소분류"]
        detail_category = category_data["세분류"]
        print(f"{category_code}, {large_category}, {medium_category}, {small_category}, {detail_category}")

    else:
        print(f"카테고리 파일 오류")
