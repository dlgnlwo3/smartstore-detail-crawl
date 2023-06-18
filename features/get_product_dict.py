if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2
from dtos.common_dto import CommonDto

from enums.product_enum import productEnum
from features.convert_delivery_company_code import *
import re
import clipboard
from features.get_notice_from_category_code import CategoryCodeConverter
from api.commerce_api import CommerceAPI
from copy import deepcopy
from common.catalog_util import get_catalog_from_product_name
from dtos.gui_dto import GUIDto


class GetProductDict:
    def __init__(self):
        product = productEnum.PRODUCT.value
        self.product = deepcopy(product)
        print(self.product)
        print()

    def get_all_categories(self, all_categories):
        self.all_categories = all_categories

    def get_addBot(self, addBot: CommerceAPI):
        self.addBot = addBot

    def get_guiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def get_product(self, commonDto: CommonDto):
        product = self.product

        # 상품 전체 정보
        originProduct: dict = product["originProduct"]
        # 이미지 정보
        images: dict = originProduct["images"]
        # 할인율
        customerBenefit: dict = originProduct["customerBenefit"]
        # 원상품 상세 속성
        detailAttribute: dict = originProduct["detailAttribute"]
        # 옵션 정보
        optionInfo: dict = detailAttribute["optionInfo"]
        # 배송 정보
        deliveryInfo: dict = originProduct["deliveryInfo"]
        # 상품정보제공고시
        productInfoProvidedNotice: dict = detailAttribute["productInfoProvidedNotice"]
        # 카탈로그
        naverShoppingSearchInfo: dict = detailAttribute["naverShoppingSearchInfo"]
        # 스마트스토어 채널 상품
        smartstoreChannelProduct: dict = product["smartstoreChannelProduct"]
        # 상품속성
        productAttributes: dict = detailAttribute["productAttributes"]

        # 카테고리가 숫자형이 아니라면 카테고리코드로 변환하는 작업
        if commonDto.leafCategoryId.isdigit() == False:

            try:
                # 카테고리 코드 변환 작업
                commonDto.leafCategoryId = list(
                    filter(lambda item: item["wholeCategoryName"] == commonDto.leafCategoryId, self.all_categories)
                )[0]["id"]
            except Exception as e:
                print(e)
                commonDto.leafCategoryId = ""

        print(f"leafCategoryId: {commonDto.leafCategoryId}")

        originProduct.update({"leafCategoryId": commonDto.leafCategoryId})

        # 상품명
        originProduct.update({"name": commonDto.name})

        # [할인 전 가격]이 빈칸이 아닌 경우
        if commonDto.before_discount_price != "" and commonDto.before_discount_price != "0":
            print("할인 적용")
            originProduct.update({"salePrice": int(commonDto.before_discount_price)})

            # 할인율
            customerBenefit.update(
                {
                    "immediateDiscountPolicy": {
                        "discountMethod": {
                            "value": int(commonDto.before_discount_price) - int(commonDto.salePrice),
                            "unitType": "WON",
                        },  # 할인
                        "mobileDiscountMethod": {
                            "value": int(commonDto.before_discount_price) - int(commonDto.salePrice),
                            "unitType": "WON",
                        },  # 할인
                    }
                }
            )
        elif commonDto.before_discount_price == "" or commonDto.before_discount_price == "0":
            # 판매가
            originProduct.update({"salePrice": int(commonDto.salePrice)})

        # 옵션
        print(f"have_option: {commonDto.have_option}")
        print(f"optionGroupNames: {commonDto.optionGroupNames}")
        print(f"optionNames: {commonDto.optionNames}")
        print(f"optionPrices: {commonDto.optionPrices}")
        print(f"optionStockQuantity: {commonDto.optionStockQuantity}")

        if commonDto.have_option and len(commonDto.optionGroupNames) > 0:
            optionCombinationGroupNames = self.convert_option_group(commonDto)
            optionCombinations = self.convert_option_combinations(commonDto)
            optionInfo.update(optionCombinationGroupNames)
            optionInfo.update({"optionCombinations": optionCombinations})
        else:
            detailAttribute["optionInfo"] = {}

        # 재고수량
        originProduct.update({"stockQuantity": int(commonDto.stockQuantity)})

        # 대표이미지, 추가이미지
        images.update(
            {
                "representativeImage": {"url": commonDto.representativeImageUrl},  # 대표이미지
                "optionalImages": commonDto.optionalImagesUrls,
            }
        )

        # 상세설명 및 상세이미지
        detailContent = self.get_detail_content(commonDto=commonDto)
        originProduct.update({"detailContent": detailContent})

        # 미성년자구매
        detailAttribute.update({"minorPurchasable": bool(commonDto.minorPurchasable)})

        # 판매자 코드 설정
        detailAttribute.update({"sellerCodeInfo": {"sellerManagementCode": f"{commonDto.sellerManagementCode}"}})

        # 상품상세정보제공고시
        if commonDto.leafCategoryId:
            print("카테고리코드 -> 상품상세정보제공고시")
            notice = CategoryCodeConverter(commonDto.leafCategoryId, self.all_categories).get_notice()

        # productInfoProvidedNotice.update(ProductInfoProvidedNotice.ETC.value)
        productInfoProvidedNotice.update(notice)

        # 택배사 코드
        deliveryCompany = commonDto.deliveryCompany
        deliveryCompany = DeliveryCompanyConverter().convert_delivery_company(deliveryCompany)
        print(deliveryCompany)
        deliveryInfo.update({"deliveryCompany": f"{deliveryCompany}"})

        # 배송비
        # 도서/산간 옵션 "deliveryFeeByArea": {"deliveryAreaType": "AREA_3", "area2extraFee": 4000, "area3extraFee": 5000},
        if commonDto.baseFee == "" or commonDto.baseFee == "0":
            deliveryInfo.update(
                {
                    "deliveryFee": {
                        "deliveryFeeType": "FREE",
                        "baseFee": 0,
                        "deliveryFeeByArea": {
                            "deliveryAreaType": "AREA_3",
                            "area2extraFee": 4000,
                            "area3extraFee": 5000,
                        },
                    },
                }
            )
        else:
            deliveryInfo.update(
                {
                    "deliveryFee": {
                        "deliveryFeeType": "PAID",
                        "baseFee": int(commonDto.baseFee),
                        "deliveryFeePayType": "PREPAID",
                        "deliveryFeeByArea": {
                            "deliveryAreaType": "AREA_3",
                            "area2extraFee": 4000,
                            "area3extraFee": 5000,
                        },
                    }
                }
            )

        # 판매자설정코드
        detailAttribute.update({"sellerCodeInfo": {"sellerManagementCode": commonDto.sellerManagementCode}})

        # 검색설정
        # tags_to_dict = self.get_sellerTags(commonDto.sellerTags)
        # detailAttribute.update({"sellerTags": tags_to_dict})
        # print(product)

        # clipboard.copy(str(product))

        # 카탈로그 검색 관련
        if self.guiDto.catalog_search == True:
            catalog_info = get_catalog_from_product_name(commonDto.name, self.addBot)
            if catalog_info != "":
                naverShoppingSearchInfo.update(
                    {
                        "modelId": catalog_info["id"],
                        "manufacturerName": catalog_info["manufacturerName"],
                        "brandName": catalog_info["brandName"],
                        "modelName": catalog_info["name"],
                    }
                )
                smartstoreChannelProduct.update({"channelProductName": catalog_info["name"]})
                print()

        # # 상품속성
        # if commonDto.detail_attribute != "":
        #     print(commonDto.detail_attribute)
        #     attribute_values = self.get_attribute_values(commonDto)
        #     productAttributes.update(attribute_values)

        return product

    # detailContent
    # 상세정보 -> 고객의 요구사항에 맞춰서 수정
    def get_detail_content(self, commonDto: CommonDto):
        image_tag = ""

        if len(commonDto.detailImagesUrls) > 0:
            for detailImagesUrl in commonDto.detailImagesUrls:
                image_tag += f'<br /> <p style="text-align: center;"> <img src="{detailImagesUrl}" alt="" class="se-image-resource"> </p>'

        detailContent = commonDto.detailContent
        body = re.search("<p.*/p>", detailContent, re.I | re.S)

        if body is None:
            print(f"html 태그가 아닙니다.")
            # detailContent = f"<br /> <p style='text-align: center;'> <img src='{commonDto.representativeImageUrl}' alt='' class='se-image-resource'> </p>{image_tag}"
            detailContent = f"<br /> <p style='text-align: center;'>{image_tag}</p>"
        else:
            print(f"html 태그 입니다.")
            detailContent = commonDto.detailContent
            detailContent = detailContent.replace("<BR><BR><BR><BR>", f"<BR><BR><BR><BR> {image_tag} <BR><BR><BR><BR>")
            print(detailContent)

        return detailContent

    # 검색설정 (해시태그)
    def get_sellerTags(self, sellerTags: str):
        tags_to_dict = []
        if sellerTags != "":
            sellerTags = sellerTags.split(",")
            for tag in sellerTags:
                tags_to_dict.append({"text": tag})
            print(tags_to_dict)
        return tags_to_dict

    # 옵션그룹
    def convert_option_group(self, commonDto: CommonDto):
        print(f"optionGroupNames: {commonDto.optionGroupNames}")
        optionGroupNames = commonDto.optionGroupNames.split(";")

        optionCombinationGroupNames = {"optionCombinationGroupNames": {}}
        option_groups_dict = {}
        for i, option_group_name in enumerate(optionGroupNames):
            option_groups_dict.update({f"optionGroupName{i+1}": option_group_name})
        print(option_groups_dict)
        optionCombinationGroupNames.update({"optionCombinationGroupNames": option_groups_dict})
        print(optionCombinationGroupNames)
        return optionCombinationGroupNames

    # 옵션정보
    def convert_option_combinations(self, commonDto: CommonDto):
        print(f"optionNames: {commonDto.optionNames}")
        print(f"optionPrices: {commonDto.optionPrices}")
        print(f"optionStockQuantity: {commonDto.optionStockQuantity}")

        optionCombinations = []
        optionNames = commonDto.optionNames.split(";")
        optionPrices = commonDto.optionPrices.split(";")
        optionStockQuantity = commonDto.optionStockQuantity

        for i, option_name in enumerate(optionNames):
            print(f"{i} {option_name} {optionPrices[i]} {optionStockQuantity}")

            option_combination = {}

            option_name = option_name.split(",")
            for j, option in enumerate(option_name):
                # 품절이라는 단어 있을 시 못들어감
                option = option.replace(" (품절)", "")
                option = option.replace("(품절)", "")
                option = option.replace("품절", "")
                option = option[:25]
                option_combination.update({f"optionName{j+1}": option})
            option_combination.update({"stockQuantity": optionStockQuantity})

            if commonDto.salePrice:
                half_price = int(commonDto.salePrice) / 2
                half_price = int(half_price)

                if optionPrices[i] == "":
                    optionPrices[i] = 0

                if abs(int(optionPrices[i])) > abs(half_price):
                    optionPrices[i] = half_price

            option_combination.update({"price": optionPrices[i]})
            option_combination.update({"usable": True})
            print(option_combination)

            optionCombinations.append(option_combination)

        print(optionCombinations)

        return optionCombinations

    # 상품속성
    def get_attribute_values(self, commonDto: CommonDto):
        print(f"leafCategoryId: {commonDto.leafCategoryId}")
        print(f"detail_attribute: {commonDto.detail_attribute}")
        attribute_values = []

        # 카테고리코드로 입력 가능한 상품속성을 검색합니다.
        attribute_data = self.addBot.get_product_attribute_values_from_category_id(commonDto.leafCategoryId)
        # print(attribute_data)

        detail_attribute_list = commonDto.detail_attribute.split(";")
        print(detail_attribute_list)

        for i, detail_attribute in enumerate(detail_attribute_list):
            print(f"{i}, {detail_attribute}")

            try:
                attribute = next(x for x in attribute_data if x["minAttributeValue"] == detail_attribute)
                print(attribute)
                print()
            except Exception as e:
                print(e)
                continue

        return attribute_values
