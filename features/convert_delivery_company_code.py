if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2

from common.utils import global_log_append


class DeliveryCompanyConverter:
    def __init__(self):
        print(f"택배사 전환")

    # 택배사 코드로 전환
    def convert_delivery_company(self, delivery_company: str):
        print(f"{delivery_company}")

        if delivery_company == "CJ대한통운" or delivery_company == "CJ 대한통운":
            delivery_company = "CJGLS"
        elif delivery_company == "로젠택배":
            delivery_company = "KGB"
        elif delivery_company == "우체국택배":
            delivery_company = "EPOST"
        elif delivery_company == "우편등기":
            delivery_company = "REGISTPOST"
        elif delivery_company == "한진택배":
            delivery_company = "HANJIN"
        elif delivery_company == "롯데택배":
            delivery_company = "HYUNDAI"
        elif delivery_company == "대신택배":
            delivery_company = "DAESIN"
        elif delivery_company == "일양로지스":
            delivery_company = "ILYANG"
        elif delivery_company == "경동택배":
            delivery_company = "KDEXP"
        elif delivery_company == "천일택배":
            delivery_company = "CHUNIL"
        elif delivery_company == "기타택배" or delivery_company == "기타 택배":
            delivery_company = "CH1"
        elif delivery_company == "GSPostbox 택배" or delivery_company == "GSPostbox택배" or delivery_company == "GSPostbox":
            delivery_company = "CVSNET"
        elif delivery_company == "DHL":
            delivery_company = "DHL"
        elif delivery_company == "FEDEX":
            delivery_company = "FEDEX"
        elif delivery_company == "GSMNTON":
            delivery_company = "GSMNTON"
        elif delivery_company == "워펙스코리아":
            delivery_company = "WARPEX"
        elif delivery_company == "WIZWA":
            delivery_company = "WIZWA"
        elif delivery_company == "EMS":
            delivery_company = "EMS"
        elif delivery_company == "DHL(독일)":
            delivery_company = "DHLDE"
        elif delivery_company == "ACI":
            delivery_company = "ACIEXPRESS"
        elif delivery_company == "EZUSA":
            delivery_company = "EZUSA"
        elif delivery_company == "범한판토스":
            delivery_company = "PANTOS"
        elif delivery_company == "UPS":
            delivery_company = "UPS"
        elif delivery_company == "롯데글로벌로지스(국제택배)":
            delivery_company = "HLCGLOBAL"
        elif delivery_company == "CJ 대한통운(국제택배)" or delivery_company == "CJ대한통운(국제택배)":
            delivery_company = "KOREXG"
        elif delivery_company == "TNT":
            delivery_company = "TNT"
        elif delivery_company == "성원글로벌":
            delivery_company = "SWGEXP"
        elif delivery_company == "대운글로벌":
            delivery_company = "DAEWOON"
        elif delivery_company == "USPS":
            delivery_company = "USPS"
        elif delivery_company == "i-parcel":
            delivery_company = "IPARCEL"
        elif delivery_company == "건영택배":
            delivery_company = "KUNYOUNG"
        elif delivery_company == "한의사랑택배":
            delivery_company = "HPL"
        elif delivery_company == "SLX 택배" or delivery_company == "SLX택배":
            delivery_company = "SLX"
        elif delivery_company == "호남택배":
            delivery_company = "HONAM"
        elif delivery_company == "GSI 익스프레스" or delivery_company == "GSI익스프레스":
            delivery_company = "GSIEXPRESS"
        elif delivery_company == "세방택배":
            delivery_company = "SEBANG"
        elif delivery_company == "농협택배":
            delivery_company = "NONGHYUP"
        elif delivery_company == "CU 편의점택배" or delivery_company == "CU편의점택배":
            delivery_company = "CUPARCEL"
        elif delivery_company == "AIRWAY 익스프레스" or delivery_company == "AIRWAY익스프레스":
            delivery_company = "AIRWAY"
        elif delivery_company == "홈픽택배":
            delivery_company = "HOMEPICK"
        elif delivery_company == "APEX":
            delivery_company = "APEX"
        elif delivery_company == "CwayExpress":
            delivery_company = "CWAYEXPRESS"
        elif delivery_company == "용마로지스":
            delivery_company = "YONGMA"
        elif delivery_company == "EuroParcel":
            delivery_company = "EUROPARCEL"
        elif delivery_company == "로젝스":
            delivery_company = "KGSL"
        elif delivery_company == "GOS 당일택배" or delivery_company == "GOS당일택배":
            delivery_company = "GOS"
        elif delivery_company == "GS Postbox 퀵" or delivery_company == "GSPostbox퀵":
            delivery_company = "GSPOSTBOX"
        elif delivery_company == "ADC 항운택배" or delivery_company == "ADC항운택배":
            delivery_company = "ADCAIR"
        elif delivery_company == "동강물류":
            delivery_company = "DONGGANG"
        elif delivery_company == "경인택배":
            delivery_company = "KIN"
        elif delivery_company == "한우리물류":
            delivery_company = "HANWOORI"
        elif delivery_company == "LG 전자물류" or delivery_company == "LG전자물류":
            delivery_company = "LGLOGISTICS"
        elif delivery_company == "일반우편":
            delivery_company = "GENERALPOST"
        elif delivery_company == "한달음택배":
            delivery_company = "HANDALUM"
        elif delivery_company == "하우저택배":
            delivery_company = "HOWSER"
        elif delivery_company == "우리동네택배":
            delivery_company = "WEVILL"
        elif delivery_company == "ACE Express" or delivery_company == "ACEExpress":
            delivery_company = "ACE"
        elif delivery_company == "큐익스프레스":
            delivery_company = "QXPRESS"
        elif delivery_company == "라인익스프레스":
            delivery_company = "LINEEXP"
        elif delivery_company == "스마트로지스":
            delivery_company = "SMARTLOGIS"
        elif delivery_company == "대림통운":
            delivery_company = "DAELIM"
        elif delivery_company == "은하쉬핑":
            delivery_company = "EUNHA"
        elif delivery_company == "홈이노베이션로지스":
            delivery_company = "HOMEINNO"
        elif delivery_company == "HI 택배" or delivery_company == "HI택배":
            delivery_company = "HYBRID"
        elif delivery_company == "우리한방택배":
            delivery_company = "WOORIHB"
        elif delivery_company == "YJS 글로벌" or delivery_company == "YJS글로벌":
            delivery_company = "YJSWORLD"
        elif delivery_company == "YJS 글로벌(영국)":
            delivery_company = "YJS"
        elif delivery_company == "시알로지텍":
            delivery_company = "CRLX"
        elif delivery_company == "애니트랙":
            delivery_company = "ANYTRACK"
        elif delivery_company == "브릿지로지스":
            delivery_company = "BRIDGE"
        elif delivery_company == "GPS LOGIX" or delivery_company == "GPSLOGIX":
            delivery_company = "GPSLOGIX"
        elif delivery_company == "에스더쉬핑":
            delivery_company = "ESTHER"
        elif delivery_company == "로토스":
            delivery_company = "LOTOS"
        elif delivery_company == "유프레이트코리아":
            delivery_company = "UFREIGHT"
        elif delivery_company == "IK물류" or delivery_company == "IK 물류":
            delivery_company = "IK"
        elif delivery_company == "성훈물류":
            delivery_company = "SUNGHUN"

        if not delivery_company:
            delivery_company = "CJGLS"

        return delivery_company
