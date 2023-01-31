if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class DietFoodInfo(Enum):
    코스트호 = {
        "originProduct": {
            "statusType": "SALE",
            "saleType": "NEW",
            "leafCategoryId": "50002615",  # 카테고리
            "name": "",  # 상품명
            "images": {
                "representativeImage": {"url": ""},  # 대표이미지
                "optionalImages": [{"url": ""}],  # 추가이미지
            },
            "detailContent": "상세설명 테스트입니다.",  # 상세설명
            "salePrice": 100000,  # 판매가
            "stockQuantity": 1,  # 재고수량
            "deliveryInfo": {
                "deliveryType": "DELIVERY",
                "deliveryAttributeType": "NORMAL",
                "deliveryCompany": "CJGLS",  # 택배사코드
                "deliveryBundleGroupUsable": True,
                "deliveryBundleGroupId": 53641574,
                "deliveryFee": {"deliveryFeeType": "PAID", "baseFee": 3500, "deliveryFeePayType": "PREPAID"},
                "claimDeliveryInfo": {
                    "returnDeliveryCompanyPriorityType": "PRIMARY",
                    "returnDeliveryFee": 3500,
                    "exchangeDeliveryFee": 7000,
                    "shippingAddressId": 105264847,
                    "returnAddressId": 105264847,
                    "freeReturnInsuranceYn": False,
                },
                "installationFee": False,
            },
            "detailAttribute": {
                "afterServiceInfo": {
                    "afterServiceTelephoneNumber": "010-9938-6536",
                    "afterServiceGuideContent": "문의사항은 해당 전화번호로 연락주십시요",
                },
                "originAreaInfo": {"originAreaCode": "03", "content": "상세설명에 표시", "plural": False},  # 원산지코드
                "optionInfo": {
                    "simpleOptionSortType": "CREATE",
                    "optionSimple": [],
                    "optionCustom": [],
                    "optionCombinationSortType": "CREATE",
                    "optionCombinations": [],
                    "standardOptionGroups": [],
                    "useStockManagement": True,
                    "optionDeliveryAttributes": [],
                },
                "supplementProductInfo": {"sortType": "CREATE", "supplementProducts": []},
                "purchaseReviewInfo": {"purchaseReviewExposure": True},
                "taxType": "TAX",
                "certificationTargetExcludeContent": {},
                "sellerCommentUsable": False,
                "minorPurchasable": True,
                "productInfoProvidedNotice": {
                    "productInfoProvidedNoticeType": "DIET_FOOD",
                    "dietFood": {
                        "returnCostReason": "0",
                        "noRefundReason": "0",
                        "qualityAssuranceStandard": "0",
                        "compensationProcedure": "0",
                        "troubleShootingContents": "0",
                        "productName": "상품상세참조",
                        "producer": "상품상세참조",
                        "location": "상품상세참조",
                        "expirationDateText": "상품상세참조",
                        "consumptionDateText": "상품상세참조",
                        "storageMethod": "상품상세참조",
                        "weight": "상품상세참조",
                        "amount": "상품상세참조",
                        "ingredients": "상품상세참조",
                        "nutritionFacts": "상품상세참조",
                        "specification": "상품상세참조",
                        "cautionAndSideEffect": "상품상세참조",
                        "nonMedicinalUsesMessage": "상품상세참조",
                        "geneticallyModified": True,
                        "importDeclarationCheck": True,
                        "consumerSafetyCaution": "상품상세참조",
                        "customerServicePhoneNumber": "상품상세참조",
                    },
                },
                "itselfProductionProductYn": False,
                "seoInfo": {"sellerTags": []},  # 해시태그
            },
            "customerBenefit": {  # 할인율
                "immediateDiscountPolicy": {
                    "discountMethod": {"value": 10, "unitType": "PERCENT"},
                    "mobileDiscountMethod": {"value": 10, "unitType": "PERCENT"},
                }
            },
        },
        "smartstoreChannelProduct": {
            "storeKeepExclusiveProduct": False,
            "naverShoppingRegistration": True,
            "channelProductDisplayStatusType": "ON",
        },
    }
