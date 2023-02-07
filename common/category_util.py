import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#!/usr/bin/env python
from http import HTTPStatus
import os
from common.utils import get_mime_type
from api.naver_shop import NaverShopAPI


def get_category_id_by_product_name(product_name: str, all_categories: dict, naverBot: NaverShopAPI):

    category_id = ""

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
    print()
