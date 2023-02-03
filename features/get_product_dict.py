if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2
from common.utils import global_log_append
from dtos.common_dto import CommonDto

from enums.product_enum import productEnum
from features.convert_delivery_company_code import *
import time
import re
import clipboard
import json
from enums.product_info_provided_notice_enum import productInfoProvidedNotice


class GetProductDict:
    def __init__(self):
        self.product = productEnum.코스트호.value
        print()

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

        # 카테고리
        originProduct.update({"leafCategoryId": commonDto.leafCategoryId})

        # 상품명
        originProduct.update({"name": commonDto.name})

        # 판매가
        originProduct.update({"salePrice": int(commonDto.salePrice)})

        # 할인율
        # customerBenefit.update(
        #     {
        #         "immediateDiscountPolicy": {
        #             "discountMethod": {
        #                 "value": int(commonDto.discountMethod),
        #                 "unitType": "PERCENT",
        #             },  # 할인율
        #             "mobileDiscountMethod": {
        #                 "value": int(commonDto.discountMethod),
        #                 "unitType": "PERCENT",
        #             },  # 할인율
        #         }
        #     }
        # )

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

        # 상품상세정보제공고시
        if commonDto.leafCategoryId == "":
            print("상품상세정보제공고시 관련해서 카테고리를 조회해야함")

        productInfoProvidedNotice = productInfoProvidedNotice

        # 택배사 코드
        deliveryCompany = commonDto.deliveryCompany
        deliveryCompany = DeliveryCompanyConverter().convert_delivery_company(deliveryCompany)
        print(deliveryCompany)
        deliveryInfo.update({"deliveryCompany": f"{deliveryCompany}"})

        # 배송비
        if commonDto.baseFee == "" or commonDto.baseFee == "0":
            deliveryInfo.update({"deliveryFee": {"deliveryFeeType": "FREE", "baseFee": 0}})
        else:
            deliveryInfo.update(
                {
                    "deliveryFee": {
                        "deliveryFeeType": "PAID",
                        "baseFee": int(commonDto.baseFee),
                        "deliveryFeePayType": "PREPAID",
                    }
                }
            )

        # 판매자설정코드
        detailAttribute.update({"sellerCodeInfo": {"sellerManagementCode": commonDto.sellerManagementCode}})

        # 검색설정
        # tags_to_dict = self.get_sellerTags(commonDto.sellerTags)
        # detailAttribute.update({"sellerTags": tags_to_dict})
        print(product)

        clipboard.copy(str(product))

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
            detailContent = f'<p><span style="font-size: 12pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"><strong><br /><br />상세설명 테스트<br />상품 품절시 (발송불가) 문자나 전화로 안내를 드리고 취소진행을 해드리고있습니다.<br />구매시 참고바랍니다. <br /><br /><br />{commonDto.name}</strong></span></p><br /><br /><p style="line-height: 3"><strong>각종 정보 입력<br />br태그로 행 구분 <br />ㅇㅇ <br />1234 <br /> </strong><br /></p><p><span style="font-size: 15pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"><strong>소개</strong></span></p><br />{commonDto.detailContent}<br /><br /><br /><p><span style="font-size: 15pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)">  </span></p><br /> {image_tag} <br /><p><span style="font-size: 15pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"></span></p><br /><br />'
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
