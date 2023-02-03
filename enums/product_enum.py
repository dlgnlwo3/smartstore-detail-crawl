if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class productEnum(Enum):

    PRODUCT = {
        "originProduct": {
            "statusType": "SALE",  # 상품 판매 상태 코드 -> 상품 등록 시에는 SALE만 입력 가능
            "saleType": "NEW",  # 상품 판매 유형 코드 -> NEW(새 상품), OLD(중고 상품)
            "leafCategoryId": "string",  # 카테고리 ID
            "name": "string",  # 상품명
            "images": {
                "representativeImage": {"url": "string"},
                "optionalImages": [{"url": "string"}],
            },  # 대표이미지, 추가이미지
            "detailContent": " ",  # 상품 상세 정보 (필수)
            "salePrice": 0,  # 판매가
            "stockQuantity": 0,  # 재고 수량
            # 배송 관련
            "deliveryInfo": {
                "deliveryType": "DELIVERY",  # 배송 방법 유형 코드 -> DELIVERY(택배, 소포, 등기), DIRECT(직접배송(화물배달))
                "deliveryAttributeType": "NORMAL",  # 배송 속성 타입 코드 -> NORMAL(일반 배송), TODAY(오늘출발)
                "deliveryCompany": "string",  # 택배사코드
                "deliveryBundleGroupUsable": True,  # 묶음배송 가능 여부
                "deliveryBundleGroupId": None,  # 묶음배송 그룹 코드 -> 묶음배송 가능이 true이고 묶음배송 그룹 코드가 null이면 기본 그룹으로 저장됩니다.
                "deliveryFee": {
                    "deliveryFeeType": "FREE",  # 배송비 타입 -> FREE(무료), CONDITIONAL_FREE(조건부 무료), PAID(유료)
                    "baseFee": 0,  # 기본 배송비
                    "freeConditionalAmount": 0,  # 무료 조건 금액
                    "deliveryFeePayType": "PREPAID",  # 배송비 결제 방식 -> COLLECT(착불), PREPAID(선결제), COLLECT_OR_PREPAID(착불 또는 선결제)
                    # 지역별 추가 배송비 -> AREA_2(내륙/제주 및 도서산간 지역으로 구분(2권역)), AREA_3(내륙/제주/제주 외 도서산간 지역으로 구분(3권역))
                    "deliveryFeeByArea": {"deliveryAreaType": "AREA_3", "area2extraFee": 20000, "area3extraFee": 30000},
                    # "differentialFeeByArea": "string",
                },
                "claimDeliveryInfo": {
                    "returnDeliveryCompanyPriorityType": "PRIMARY",  # 반품 택배사 우선순위 타입 -> 미입력 시 '기본 반품 택배사(PRIMARY)'로 설정됩니다.
                    "returnDeliveryFee": 3500,  # 반품 배송비 -> (배송비)
                    "exchangeDeliveryFee": 7000,  # 교환 배송비 -> (배송비*2)
                    # "shippingAddressId": '',  # 출고지 주소록 번호
                    # "returnAddressId": '',  # 반품/교환지 주소록 번호
                    "freeReturnInsuranceYn": False,  # 반품안심케어 설정
                },
                "installationFee": False,  # 별도 설치비 유무
            },
            # 원상품 상세 속성
            "detailAttribute": {
                # A/S전화번호, A/S안내
                "afterServiceInfo": {
                    "afterServiceTelephoneNumber": "010-1234-5678",
                    "afterServiceGuideContent": "A/S 관련 안내 사항입니다.",
                },
                # 원산지 정보
                "originAreaInfo": {"originAreaCode": "04", "content": "상세설명에 표시", "plural": False},
                # ★ 옵션 정보 ★
                "optionInfo": {
                    # 단독형 옵션
                    "simpleOptionSortType": "CREATE",
                    "optionSimple": [],
                    "optionCustom": [],
                    # 조합형 옵션
                    "optionCombinationSortType": "CREATE",
                    # 조합형 옵션명 목록 optionGroupName1... optionGroupName2...
                    # "optionCombinationGroupNames": {},
                    # 조합형 옵션
                    "optionCombinations": [],
                    "standardOptionGroups": [],
                    "useStockManagement": True,  # 옵션 재고 수량 관리 사용 여부
                    "optionDeliveryAttributes": [],  # 옵션별 배송 속성 옵션값 목록
                },
                # 추가 상품
                "supplementProductInfo": {
                    "sortType": "CREATE",
                    "supplementProducts": [],
                },
                # 리뷰 노출 설정, 리뷰 미노출 사유 -> 식품 카테고리에만 False 사용 가능, False일 경우 사유 입력
                "purchaseReviewInfo": {"purchaseReviewExposure": True, "reviewUnExposeReason": ""},
                # 부가가치세 타입 코드 -> TAX(과세 상품), DUTYFREE(면세 상품), SMALL(영세 상품)
                "taxType": "TAX",
                # 판매자 특이사항
                "sellerCommentUsable": False,
                # 미성년자 구매 가능 여부
                "minorPurchasable": True,
                # 상품정보제공고시 -> product_info_provided_notice_enum 사용
                "productInfoProvidedNotice": {},
                # 상품 속성 목록
                "productAttributes": [],
            },
            # 고객 혜택 정보
            "customerBenefit": {},
        },
        # 스마트스토어 채널 상품
        "smartstoreChannelProduct": {
            # 알림받기 동의 회원 전용 상품
            "storeKeepExclusiveProduct": False,
            # 네이버쇼핑 등록 여부
            "naverShoppingRegistration": True,
            # 전시 상태 코드 -> WAIT(전시 대기), ON(전시 중), SUSPENSION(전시 중지)
            "channelProductDisplayStatusType": "ON",
        },
    }

    코스트호 = {
        "originProduct": {
            "statusType": "SALE",  # 상품 판매 상태 코드 -> 상품 등록 시에는 SALE만 입력 가능
            "saleType": "NEW",  # 상품 판매 유형 코드 -> NEW(새 상품), OLD(중고 상품)
            "leafCategoryId": "string",  # 카테고리 ID
            "name": "string",  # 상품명
            "images": {
                "representativeImage": {"url": "string"},
                "optionalImages": [{"url": "string"}],
            },  # 대표이미지, 추가이미지
            "detailContent": " ",  # 상품 상세 정보 (필수)
            "salePrice": 0,  # 판매가
            "stockQuantity": 0,  # 재고 수량
            # 배송 관련
            "deliveryInfo": {
                "deliveryType": "DELIVERY",  # 배송 방법 유형 코드 -> DELIVERY(택배, 소포, 등기), DIRECT(직접배송(화물배달))
                "deliveryAttributeType": "NORMAL",  # 배송 속성 타입 코드 -> NORMAL(일반 배송), TODAY(오늘출발)
                "deliveryCompany": "string",  # 택배사코드
                "deliveryBundleGroupUsable": True,  # 묶음배송 가능 여부
                "deliveryBundleGroupId": int,  # 묶음배송 그룹 코드 -> 묶음배송 가능이 true이고 묶음배송 그룹 코드가 null이면 기본 그룹으로 저장됩니다.
                "deliveryFee": {
                    "deliveryFeeType": "FREE",  # 배송비 타입 -> FREE(무료), CONDITIONAL_FREE(조건부 무료), PAID(유료)
                    "baseFee": 0,  # 기본 배송비
                    "freeConditionalAmount": 0,  # 무료 조건 금액
                    # "repeatQuantity": 0,
                    # "secondBaseQuantity": 0,
                    # "secondExtraFee": 0,
                    # "thirdBaseQuantity": 0,
                    # "thirdExtraFee": 0,
                    "deliveryFeePayType": "PREPAID",  # 배송비 결제 방식 -> COLLECT(착불), PREPAID(선결제), COLLECT_OR_PREPAID(착불 또는 선결제)
                    # 지역별 추가 배송비 -> AREA_2(내륙/제주 및 도서산간 지역으로 구분(2권역)), AREA_3(내륙/제주/제주 외 도서산간 지역으로 구분(3권역))
                    "deliveryFeeByArea": {"deliveryAreaType": "AREA_3", "area2extraFee": 20000, "area3extraFee": 30000},
                    # "differentialFeeByArea": "string",
                },
                "claimDeliveryInfo": {
                    "returnDeliveryCompanyPriorityType": "PRIMARY",  # 반품 택배사 우선순위 타입 -> 미입력 시 '기본 반품 택배사(PRIMARY)'로 설정됩니다.
                    "returnDeliveryFee": 3500,  # 반품 배송비 -> (배송비)
                    "exchangeDeliveryFee": 7000,  # 교환 배송비 -> (배송비*2)
                    "shippingAddressId": 105264847,  # 출고지 주소록 번호
                    "returnAddressId": 105264847,  # 반품/교환지 주소록 번호
                    "freeReturnInsuranceYn": False,  # 반품안심케어 설정
                },
                "installationFee": False,  # 별도 설치비 유무
                # "expectedDeliveryPeriodType": "ETC",  # 주문제작
                # "expectedDeliveryPeriodDirectInput": "string",# 주문제작
                # "todayStockQuantity": 0,  # 오늘출발 상품 재고 수량
                # "customProductAfterOrderYn": True, # 주문 확인 후 제작
                # "hopeDeliveryGroupId": 0,  # 희망일배송 그룹 번호
            },
            # 풀필먼트 관련
            # "productLogistics": [{"logisticsCompanyId": "string", "logisticsCenterId": "string"}],
            # 원상품 상세 속성
            "detailAttribute": {
                # 네이버쇼핑 검색 정보
                # "naverShoppingSearchInfo": {
                #     "modelId": 0,
                #     "manufacturerName": "string",
                #     "brandName": "string",
                #     "modelName": "string",
                # },
                # A/S전화번호, A/S안내 -> 사용자에게 입력 받아야 할 듯
                "afterServiceInfo": {
                    "afterServiceTelephoneNumber": "010-9938-6536",
                    "afterServiceGuideContent": "문의사항은 해당 전화번호로 연락주십시요",
                },
                # 구매 수량 정보
                # "purchaseQuantityInfo": {
                #     "minPurchaseQuantity": 0,  # 최소 구매 수량
                #     "maxPurchaseQuantityPerId": 0,  # 1인 최대 구매 수량
                #     "maxPurchaseQuantityPerOrder": 0,  # 1회 최대 구매 수량
                # },
                # 원산지 정보
                "originAreaInfo": {"originAreaCode": "04", "content": "상세설명에 표시", "plural": False},
                # 판매자 코드
                # "sellerCodeInfo": {
                #     "sellerManagementCode": "string",
                #     "sellerBarcode": "string",
                #     "sellerCustomCode1": "string",
                #     "sellerCustomCode2": "string",
                # },
                # ★ 옵션 정보 ★
                "optionInfo": {
                    # 단독형 옵션
                    "simpleOptionSortType": "CREATE",
                    "optionSimple": [],
                    "optionCustom": [],
                    # 조합형 옵션
                    "optionCombinationSortType": "CREATE",
                    # 조합형 옵션명 목록 optionGroupName1... optionGroupName2...
                    "optionCombinationGroupNames": {"optionGroupName1": "string", "optionGroupName2": "string"},
                    # 조합형 옵션
                    "optionCombinations": [
                        {
                            "id": 0,  # 옵션 ID
                            "optionName1": "string",  # 옵션값 1
                            "optionName2": "string",  # 옵션값 2
                            "optionName3": "string",  # 옵션값 3
                            # "optionName4": "string",  # 지점형 옵션에만 사용 -> 사용 안함
                            "stockQuantity": 0,  # 옵션별 재고 -> 미입력 시 0개
                            "price": 0,  # 옵션가
                            "sellerManagerCode": "string",  # 판매자 관리 코드
                            "usable": True,  # 사용여부
                        },
                    ],
                    "standardOptionGroups": [],
                    # "optionStandards": [],
                    "useStockManagement": True,  # 옵션 재고 수량 관리 사용 여부
                    "optionDeliveryAttributes": [],  # 옵션별 배송 속성 옵션값 목록
                },
                # 추가 상품
                "supplementProductInfo": {
                    "sortType": "CREATE",
                    "supplementProducts": [],
                },
                # 리뷰 노출 설정, 리뷰 미노출 사유 -> 식품 카테고리에만 False 사용 가능, False일 경우 사유 입력
                "purchaseReviewInfo": {"purchaseReviewExposure": True, "reviewUnExposeReason": ""},
                # ISBN 정보 (도서)
                # "isbnInfo": {"isbn13": "string", "issn": "string", "independentPublicationYn": True},
                # 도서 정보 (도서)
                # "bookInfo": {
                #     "publishDay": "string",
                #     "publisher": {"code": "string", "text": "string"},
                #     "authors": [{"code": "string", "text": "string"}],
                #     "illustrators": [{"code": "string", "text": "string"}],
                #     "translators": [{"code": "string", "text": "string"}],
                # },
                # 이벤트 문구
                # "eventPhraseCont": "string",
                # 제조 일자 -> 인증 유형이 방송통신기자재 적합인증/적합등록/잠정인증인 경우 필수.
                # "manufactureDate": "2023-01-30",
                # 유효 일자
                # "validDate": "2023-01-30",
                # 부가가치세 타입 코드 -> TAX(과세 상품), DUTYFREE(면세 상품), SMALL(영세 상품)
                "taxType": "TAX",
                # 인증 정보 목록 -> 어린이제품 인증 대상 카테고리 상품인 경우 필수
                # "productCertificationInfos": [
                #     {
                #         "certificationInfoId": 0,
                #         "certificationKindType": "KC_CERTIFICATION",
                #         "name": "string",
                #         "certificationNumber": "string",
                #         "certificationMark": True,
                #         "companyName": "string",
                #         "certificationDate": "2023-01-30",
                #     }
                # ],
                # 인증 대상 제외 여부 정보
                # "certificationTargetExcludeContent": {
                #     "childCertifiedProductExclusionYn": True,
                #     "kcExemptionType": "OVERSEAS",
                #     "kcCertifiedProductExclusionYn": "FALSE",
                #     "greenCertifiedProductExclusionYn": True,
                # },
                # 판매자 특이사항 -> sellerCommentUsable이 True일 경우 입력
                # "sellerCommentContent": "string",
                "sellerCommentUsable": False,
                # 미성년자 구매 가능 여부
                "minorPurchasable": True,
                # E쿠폰
                # "ecoupon": {
                #     "periodType": "FIXED",
                #     "validStartDate": "2023-01-30",
                #     "validEndDate": "2023-01-30",
                #     "periodDays": 0,
                #     "publicInformationContents": "string",
                #     "contactInformationContents": "string",
                #     "usePlaceType": "PLACE",
                #     "usePlaceContents": "string",
                #     "restrictCart": True,
                #     "siteName": "string",
                # },
                # 상품정보제공고시 -> product_info_provided_notice_enum 사용
                "productInfoProvidedNotice": {},
                # 상품 속성 목록
                "productAttributes": [
                    # {
                    #     "attributeSeq": 0,
                    #     "attributeValueSeq": 0,
                    #     "attributeRealValue": "string",
                    #     "attributeRealValueUnitCode": "string",
                    # }
                ],
                # 문화비 소득공제 여부 -> 미입력시 False
                # "cultureCostIncomeDeductionYn": True,
                # 맞춤 제작 상품 여부
                # "customProductYn": False,
                # 자체 제작 상품 여부
                # "itselfProductionProductYn": False,
                # 브랜드 인증 여부
                # "brandCertificationYn": False,
                # 판매자 코드 정보
                # "seoInfo": {
                #     "pageTitle": "string",
                #     "metaDescription": "string",
                #     "sellerTags": [{"code": 0, "text": "string"}],
                # },
            },
            # 고객 혜택 정보
            "customerBenefit": {},
        },
        # 스마트스토어 채널 상품
        "smartstoreChannelProduct": {
            # 채널 상품 전용 상품명 -> 미입력 시 원상품명
            # "channelProductName": "string",
            # 알림받기 동의 회원 전용 상품
            "storeKeepExclusiveProduct": False,
            # 네이버쇼핑 등록 여부
            "naverShoppingRegistration": True,
            # 공지사항 게시글 일련번호
            # "bbsSeq": 0,
            # 전시 상태 코드 -> WAIT(전시 대기), ON(전시 중), SUSPENSION(전시 중지)
            "channelProductDisplayStatusType": "ON",
        },
        # 윈도 채널 상품 -> 쇼핑 윈도우 전용
        # "windowChannelProduct": {
        #     "channelProductName": "string",
        #     "storeKeepExclusiveProduct": True,
        #     "naverShoppingRegistration": True,
        #     "bbsSeq": 0,
        #     "channelNo": 0,
        #     "best": True,
        # },
    }
