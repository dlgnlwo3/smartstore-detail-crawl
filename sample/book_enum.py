if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum


class BookInfo(Enum):
    책인감 = {
        "originProduct": {
            "statusType": "SALE",
            "saleType": "NEW",
            "leafCategoryId": "",  # 카테고리
            "name": "",  # 상품명
            "images": {
                "representativeImage": {"url": ""},  # 대표이미지
                "optionalImages": [{"url": ""}],  # 추가이미지
            },
            # 상세설명 및 상세이미지
            "detailContent": f'<p><span style="font-size: 12pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"><strong><br /><br />도서의 특성상 품절및 절판이 빈번합니다.<br />상품 품절 절판시 (발송불가) 문자나 전 화로 안내를 드리고 취소진행을 해드리고있습니다.<br />구매시 참고바랍니다. <br /><br /><br />적당히 느슨하게 조금씩 행복해지는 습관</strong></span></p><br /><br /><p style="line-height: 3"><strong>저자 : 바쿠@정신과의<br />출판사 : 부키<br />출간일 : 2023-01-11<br />ISBN : 9788960519657<br />크기(판형) : 128*188mm (B6)<br /><strong>페이지 : 264<br /><strong>분야 : </strong>마음 다스리기<br /><br /><br /></strong></strong></p><p><span style="font-size: 15pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"><strong>책소개</strong></span></p><br />의태를 좀 더 쉽게 익히기 위한 40가지 습관을 구체적이면서도 간결하게 다루고 있다. 뜬구름 잡는 위로나 휘발되고 마는 일회성 조언이 아니라 매 일 조금씩 일상에서 적용할 수 있는 노하우로 가득하다.<br /><br /><br /><p><span style="font-size: 15pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"><strong>출판사서평</strong></span></p><br /><br /><br /><br /><p><span style="font-size: 15pt; font-family: &quot;나눔고딕&quot;,NanumGothic; color: rgb(53,56,151)"><strong>목차</strong></span></p><br /><br />',
            "salePrice": int,  # 판매가
            "stockQuantity": int,  # 재고수량
            "deliveryInfo": {  # 배송관련
                "deliveryType": "DELIVERY",
                "deliveryAttributeType": "NORMAL",
                "deliveryCompany": "CJGLS",
                "deliveryBundleGroupUsable": True,
                "deliveryBundleGroupId": 8787374,
                "deliveryFee": {"deliveryFeeType": "FREE", "baseFee": 0},
                "claimDeliveryInfo": {
                    "returnDeliveryCompanyPriorityType": "PRIMARY",
                    "returnDeliveryFee": 2500,
                    "exchangeDeliveryFee": 5000,
                    "shippingAddressId": 100391514,
                    "returnAddressId": 100391515,
                    "freeReturnInsuranceYn": False,
                },
                "installationFee": False,
                "customProductAfterOrderYn": False,
            },
            "detailAttribute": {
                "afterServiceInfo": {
                    "afterServiceTelephoneNumber": "01076099922",
                    "afterServiceGuideContent": "판매자문의",
                },  # A/S 관련
                "originAreaInfo": {"originAreaCode": "04", "content": "국산", "plural": False},  # 원산지
                "sellerCodeInfo": {"sellerManagementCode": ""},  # 판매자설정코드
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
                "isbnInfo": {"isbn13": "", "independentPublicationYn": False},  # ISBN-13
                "bookInfo": {
                    "publishDay": "",  # 출간일
                    "publisher": {"text": ""},  # 출판사
                    "authors": [{"text": ""}],  # 글작가
                    "illustrators": [{"text": ""}],  # 그림작가
                    "translators": [{"text": ""}],  # 번역자명
                },
                "taxType": "DUTYFREE",
                "certificationTargetExcludeContent": {"childCertifiedProductExclusionYn": True},
                "sellerCommentUsable": False,
                "minorPurchasable": bool,  # 미성년자구매
                "productInfoProvidedNotice": {
                    "productInfoProvidedNoticeType": "BOOKS",
                    "books": {
                        "returnCostReason": "전자상거래등에서의소비자보호에관한 법률 등에 의한 제품의 하자 또는 오배송 등으로 인한 청약철회의 경우에는 상품 수령 후 3개월 이내, 그 사실을 안 날 또는 알 수 있었던 날로부터 30일 이내에 청약철회를 할 수 있으며, 반품 비용은 통신판매업자가 부담합니다.",
                        "noRefundReason": "전자상거래 등에서의 소비자보호에 관한 법률 등에 의한 청약철회 제한 사유에 해당하는 경우 및 기타 객관적으로 이에 준하 는 것으로 인정되는 경우 청약철회가 제한될 수 있습니다.",
                        "qualityAssuranceStandard": "소비자분쟁해결기준(공정거래위원회 고시) 및 관계법령에 따릅니다.",
                        "compensationProcedure": "주문취소 및 대금의 환불은 네이버페이 마이페이지에서 신청할 수 있으며, 전자상거래 등에서의 소비자보호에 관한 법률에 따라 소비자의 청약철회 후 판매자가 재화 등을 반환 받은 날로부 터 3영업일 이내에 지급받은 대금의 환급을 정당한 사유 없이 지연하는 때에는 소비자는 지연기간에 대해서 연 20%의 지연배상금을 판매자에게 청구할 수 있습니다.",
                        "troubleShootingContents": "소비자분쟁해결기준(공정거래위원회 고시) 및 관계법령에 따릅니다.",
                        "title": "상품상세참조",
                        "author": "상품상세참조",
                        "publisher": "상품상세참조",
                        "size": "상품상세참조 / 상품상세참조",
                        "pages": "상품상세참조",
                        "components": "상품상세참조",
                        "publishDateText": "상품상세참조",
                        "description": "상품상세참조",
                    },
                },
                "cultureCostIncomeDeductionYn": False,
                "customProductYn": False,
                "itselfProductionProductYn": False,
            },
            "customerBenefit": {
                "immediateDiscountPolicy": {
                    "discountMethod": {"value": int, "unitType": "PERCENT"},  # 할인율
                    "mobileDiscountMethod": {"value": int, "unitType": "PERCENT"},  # 할인율
                },
                "purchasePointPolicy": {"value": 10, "unitType": "WON"},
            },
        },
        "smartstoreChannelProduct": {
            "channelProductName": "",
            "storeKeepExclusiveProduct": False,
            "naverShoppingRegistration": True,
            "channelProductDisplayStatusType": "ON",
        },
    }

    코스트호 = {
        "originProduct": {
            "statusType": "SUSPENSION",
            "saleType": "NEW",
            "leafCategoryId": "50005732",
            "name": "도서 등록 테스트",
            "images": {
                "representativeImage": {
                    "url": "http://shop1.phinf.naver.net/20230110_115/1673324214516yGQ7U_JPEG/74460057214527052_1403962178.jpg"
                },
                "optionalImages": [],
            },
            "detailContent": '<div class="se-viewer se-theme-default" lang="ko-KR">\n    <!-- SE_DOC_HEADER_START -->\n    <!--@CONTENTS_HEADER-->\n    <!-- SE_DOC_HEADER_END -->\n    <div class="se-main-container">\n                <div class="se-component se-image se-l-default" id="SE-6bf7c693-cb3b-4c13-8759-e6cf35f6c8fb">\n                    <div class="se-component-content se-component-content-normal">\n <div class="se-section se-section-image se-l-default se-section-align-" style="max-width:700px;">\n                                <div class="se-module se-module-image" style="">\n                                    <a class="se-module-image-link __se_image_link __se_link" style="" onclick="return false;" data-linktype="img" data-linkdata="{&quot;id&quot;:&quot;SE-6bf7c693-cb3b-4c13-8759-e6cf35f6c8fb&quot;,&quot;src&quot;:&quot;https://shop-phinf.pstatic.net/20230110_95/1673324241944Ff1Rv_JPEG/8933871993_01.jpg&quot;,&quot;originalWidth&quot;:&quot;700&quot;,&quot;originalHeight&quot;:&quot;7026&quot;,&quot;linkUse&quot;:&quot;false&quot;,&quot;link&quot;:&quot;&quot;}">\n <img src="https://shop-phinf.pstatic.net/20230110_95/1673324241944Ff1Rv_JPEG/8933871993_01.jpg" alt="" class="se-image-resource">\n </a>\n                                </div>\n                        </div>\n                    </div>\n                </div>\n                <div class="se-component se-table se-l-default" id="SE-00358e34-2b38-4723-ae9c-9f1f84e85dec">\n                    <div class="se-component-content">\n                        <div class="se-section se-section-table se-l-default se-section-align-" style="width: 60%;">\n                            <div class="se-table-container">\n                                <table class="se-table-content" style="border:none;border-collapse:collapse;">\n                                    <tbody><tr class="se-tr"><td class="se-cell" colspan="1" rowspan="1" style="width: 100.0%; height: 40.0px; border:none; ">\n                                                <div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-b5aa5c70-8a05-4986-bbae-b06cce8431ba"><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-0f581627-13b4-4d4f-8587-3080ae51da6c">인생드라마가 또다시 인생책이 되다</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-69e90382-2656-45df-a8c1-eef23510085a"><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-90af1255-986c-4f57-a96f-ae44de1693c8">수많은 사람에게 10년 가까이 사랑받아온 드라마 &lt;미생&gt; 작품집 출간!</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-ee35add3-2137-46fd-b695-fcfd89d92907"><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-83800657-bff6-44ff-8b9a-08ba92187262">불안한 세상 속에서 이 름 없이 고군분투 중인 우리에게 여전히 유효한 이야기</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-19b93c3e-94c6-4f5d-a968-8358f6cceb14"><span style="" class="se-fs- se-ff-   " id="SE-b95e0342-bdde-4b46-aaa7-2b5bf310d493">\u200b</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-0adb95f4-0b44-4ea9-b246-2e150363bd78"><span style="color:#000000;" class="se-fs-fs15 se-ff-system se-style-unset " id="SE-2ba62890-386a-4d57-b3e9-787a416a6d8e">✶</span><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-44d92e7a-6d06-4687-9b33-bc4989381b6d"> 백상예술대상 연출상, 남자최우수연기상, 남자신인연기상</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-fef5ff30-9918-4c05-8719-34744cb49b62"><span style="color:#000000;" class="se-fs-fs15 se-ff-system  se-style-unset " id="SE-211c33b4-9ffd-404b-9023-4e2efd6b19f1">✶</span><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-936f2895-46de-44e0-ab02-7957d68ad2ba"> 서울드라마어워즈 최우수작품상</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-cb630aba-d486-489b-8d69-ab784a0ab634"><span style="color:#000000;" class="se-fs-fs15 se-ff-system  se-style-unset " id="SE-57e835aa-9a52-44ab-8629-bc846ab99b4c">✶</span><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-5b654619-54a1-41df-b797-72f9fec30d93"> 드라마 공식 채널 클립 2억 5천만 뷰</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-8128b888-2051-419c-8ea3-8ac3a6b92404"><span style="" class="se-fs- se-ff-   " id="SE-ca621929-b970-4cd6-bac1-baaed2a50828">\u200b</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-314b3e59-7265-4fed-a341-baada50b7a3b"><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-91144d6f-0c2a-4e9a-b779-67642ba69ed7">우리가 각자의 일터에서 고군분투하는 하루하루가 생생히 담겨 있어 그해 신드롬이 되었던 드라마 &lt;미생&gt; 작품집이 출간됐다. 좋은 반응을 얻었던 원작이라면 매체를 옮겨왔을 때 이를 바라보는 잣대가 엄격해지곤 한다. 그러나 드라마 &lt;미생&gt;은 원작에서 가져올 것은 가져오면서 이야기를 새롭고 풍성하게 직조하여 많은 이의 열광을 불러일으켰다. 드라마 방영 이후 10년 가까이 시간이 흘렀지만 여전히 우리에게는 오상식 같은 리더와 김동식 같은 동료가 필요하며, 직장인들의 삶은 팍팍하다. 이런 이유들로 사람들은 여전히 &lt;미생&gt;을 자신의 인생드라마로 간직하고 있다. 삶의 근원을 조명하기에 언제 다시 보아도 우리에게 의미를 남기는 이 이야기는 쉽고 빠르게 빛을 낼 만한 것들에 눈을 돌리지 않고 단단하게 중심을 잡아나간다. 지금까지도 드라마 필수 요소처럼 쓰이곤 하는 멜로를 &lt;미생&gt;은 과감히 배제했고, 서사 전개를 위해 쓰이 곤 하는 헛된 희망도 담지 않았다. 다만 출구 없는 답답한 삶에 갇힌 듯 느껴질 때 그래도 살아갈 수 있는 작은 힘이 결국 ‘사람’이라고 말하며 위로를 전할 뿐이다.</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-88b8f736-d0ff-43e4-99bb-2d74032c62e3"><span style="" class="se-fs- se-ff- " id="SE-a7c57a40-7951-405d-b908-4a6df75f4704">\u200b</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-242f3e36-a8c4-4e45-8c2c-f3220e94506e"><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-715f0607-f10a-425b-a609-dc21050ab546">마음을 어루만져 사 람들의 마음에 오래 남은 드라마를 하나의 책으로 엮어가는 세계사 인생드라마 작품집 &lt;미생&gt;에는 전회 대본, 작품집만을 위해 일러스트레이터 손은경이 그린 장면들이 포함되어 있고, 드라마가 만들어지는 제작기, 스틸컷과 코멘터리 등의 이야기가 수록되어 있다. 특히나 원작의 메시지와 핵심 에피소드를 유지하되 원래의 구조를 허물고 새롭게 드라마 서사로 써나가는 까 다로운 과정이 \'작가의 말\'에 면밀히 담겨 있다. 30쪽에 달하는 정윤정 작가의 솔직하고도 꾸밈없는 집필 과정은 드라마를 사랑하는 사람뿐 아니라 콘텐츠를 구성하고 글을 쓰는 사람들에 게도 큰 영감이 되어줄 것이다. 이외에도 극 중 영업3팀이었던 배우 임시완, 김대명, 이성민의 그때와 지금을 아우르는 드라마 이야기, &lt;시그널&gt; &lt;나의 아저씨&gt; 등 기록적인 작 품을 연출한 김원석 감독의 네 시간 분량 인터뷰가 각 권에 수록되어 있다.</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-434abc79-498a-4646-bff8-981b47007cf3"><span style="" class="se-fs- se-ff-   " id="SE-cfa6d37f-9a35-4f20-970c-d471f3bc9b13">\u200b</span></p></div><div class="se-module se-module-text"><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-ddcfcbd0-2854-4a2b-ac0b-37c2150eec53"><span style="color:#000000;" class="se-fs-fs15 se-ff-  se-style-unset " id="SE-4a417c75-0b86-4529-aa45-5517161dcd9b">인생드라마 작품집은 부록뿐 아니라 외적으로 다가오는 물성에도 드라마 특유의 분위기와 이미지를 온전히 담 아보고자 했다. &lt;미생&gt; 1~3권 표지는 각각의 선들이 부대끼며 원을 만들어가는 "미생에서 완생으로" 가는 과정을 표현한다. 또한 질감이 살아 있는 백색 계열 종이에 먹박만을 사용한 원인터내셔널 공간 배치도는 극 중 배경인 원인터내셔널 사무실의 무드를 그대로 담고 있으며, 북케이스 표지 정중앙에 들어간 영업3팀의 사진으로 유쾌함을 더했다.</span></p></div>\n \n                                    </td></tr></tbody>\n                                </table>\n                            </div>\n                        </div>\n                    </div>\n                    <script type="text/data" class="__se_module_data" data-module="{&quot;type&quot;:&quot;v2_table&quot;, &quot;id&quot; : &quot;SE-00358e34-2b38-4723-ae9c-9f1f84e85dec&quot;, &quot;data&quot;: { &quot;columnCount&quot; : &quot;1&quot; }}"></script>\n                </div>                <div class="se-component se-text se-l-default" id="SE-9ee4b696-1fe1-4075-8aa6-c3e41fed0b7d">\n                    <div class="se-component-content">\n                        <div class="se-section se-section-text se-l-default">\n                            <div class="se-module se-module-text">\n                                    <!-- SE-TEXT { --><p class="se-text-paragraph se-text-paragraph-align- " style="" id="SE-c5dd5449-8e91-466e-be13-fe5f20d51203"><span style="" class="se-fs- se-ff-   " id="SE-4d27f6d1-c57b-4cca-8e6c-dc0616a0b401">\u200b</span></p><!-- } SE-TEXT -->\n                            </div>\n                        </div>\n                    </div>\n                </div>    </div>\n</div>\n',
            "salePrice": 66000,
            "stockQuantity": 2,
            "deliveryInfo": {
                "deliveryType": "DELIVERY",
                "deliveryAttributeType": "NORMAL",
                "deliveryCompany": "CJGLS",
                "deliveryBundleGroupUsable": True,
                "deliveryBundleGroupId": 53641574,
                "deliveryFee": {"deliveryFeeType": "PAID", "baseFee": 3000, "deliveryFeePayType": "PREPAID"},
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
                    "afterServiceGuideContent": "문의사항은 해당 전화번호로 연락 주십시요",
                },
                "originAreaInfo": {"originAreaCode": "00", "content": "국산", "plural": False},
                "sellerCodeInfo": {"sellerManagementCode": ""},
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
                "isbnInfo": {"isbn13": "9788983948786"},
                "bookInfo": {
                    "publishDay": "2023-01-17",
                    "publisher": {"text": "세계사"},
                    "authors": [{"text": "윤태호"}],
                    "illustrators": [],
                    "translators": [],
                },
                "taxType": "TAX",
                "certificationTargetExcludeContent": {"childCertifiedProductExclusionYn": True},
                "sellerCommentUsable": False,
                "minorPurchasable": True,
                "productInfoProvidedNotice": {
                    "productInfoProvidedNoticeType": "BOOKS",
                    "books": {
                        "returnCostReason": "0",
                        "noRefundReason": "0",
                        "qualityAssuranceStandard": "0",
                        "compensationProcedure": "0",
                        "troubleShootingContents": "0",
                        "title": "상품상세참조",
                        "author": "상품상세참조",
                        "publisher": "상품상세참조",
                        "size": "상품상세참조",
                        "pages": "상품상세참조",
                        "components": "상품상세참조 ",
                        "publishDateText": "상품상세참조",
                        "description": "상품상세참조",
                    },
                },
                "cultureCostIncomeDeductionYn": True,
                "itselfProductionProductYn": False,
                "seoInfo": {"sellerTags": []},
            },
            "customerBenefit": {
                "immediateDiscountPolicy": {
                    "discountMethod": {"value": 6600, "unitType": "WON"},
                    "mobileDiscountMethod": {"value": 6600, "unitType": "WON"},
                }
            },
        },
        "smartstoreChannelProduct": {
            "channelProductName": "",
            "storeKeepExclusiveProduct": False,
            "naverShoppingRegistration": True,
            "channelProductDisplayStatusType": "SUSPENSION",
        },
    }
