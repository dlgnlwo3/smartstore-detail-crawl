if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# 공통값 DTO
class CommonDto:
    def __init__(self):

        self.__media_path = ""  # 이미지 경로
        self.__leafCategoryId = ""  # 카테고리
        self.__name = ""  # 상품명
        self.__salePrice = ""  # 판매가
        self.__discountMethod = ""  # 할인율
        self.__stockQuantity = ""  # 재고수량

        self.__representativeImage = ""  # 엑셀->대표이미지
        self.__optionalImages = []  # 엑셀->추가이미지
        self.__detailImages = []  # 엑셀->상세설명에 사용할 이미지
        self.__detailContent = ""  # 상세설명

        self.__representativeImageUrl = ""  # API->대표이미지
        self.__optionalImagesUrls = []  # API->추가이미지
        self.__detailImagesUrls = []  # API->상세설명에 사용할 이미지

        self.__minorPurchasable = bool  # 미성년자구매
        self.__deliveryCompany = ""  # 택배사코드
        self.__baseFee = ""  # 기본배송비
        self.__sellerManagementCode = ""  # 판매자 설정 코드

        self.__sellerTags = ""  # 검색설정 (해시태그)

        # 옵션관련
        self.__have_option = ""  # 옵션
        self.__optionGroupNames = ""  # 옵션그룹
        self.__optionNames = ""  # 옵션이름
        self.__optionStockQuantity = ""  # 옵션재고 ("stockQuantity": 0 형식으로 들어감)
        self.__optionPrices = ""  # 옵션가격 ("price": 0 형식으로 들어감)

    @property
    def media_path(self):  # getter
        return self.__media_path

    @media_path.setter
    def media_path(self, value):  # setter
        self.__media_path = value

    @property
    def leafCategoryId(self):  # getter
        return self.__leafCategoryId

    @leafCategoryId.setter
    def leafCategoryId(self, value):  # setter
        self.__leafCategoryId = value

    @property
    def name(self):  # getter
        return self.__name

    @name.setter
    def name(self, value):  # setter
        self.__name = value

    @property
    def salePrice(self):  # getter
        return self.__salePrice

    @salePrice.setter
    def salePrice(self, value):  # setter
        self.__salePrice = value

    @property
    def discountMethod(self):  # getter
        return self.__discountMethod

    @discountMethod.setter
    def discountMethod(self, value):  # setter
        self.__discountMethod = value

    @property
    def stockQuantity(self):  # getter
        return self.__stockQuantity

    @stockQuantity.setter
    def stockQuantity(self, value):  # setter
        self.__stockQuantity = value

    @property
    def representativeImage(self):  # getter
        return self.__representativeImage

    @representativeImage.setter
    def representativeImage(self, value):  # setter

        if value != "":
            value = os.path.join(self.media_path, self.name, value)

        self.__representativeImage = value

    @property
    def optionalImages(self):  # getter
        return self.__optionalImages

    @optionalImages.setter
    def optionalImages(self, value: str):  # setter
        option_img_list = []
        if value != "":
            option_imgs = value.split(",")
            for option_img in option_imgs:
                option_img_list.append(os.path.join(self.media_path, self.name, option_img))
        self.__optionalImages = option_img_list

    @property
    def detailImages(self):  # getter
        return self.__detailImages

    @detailImages.setter
    def detailImages(self, value: str):  # setter
        detail_img_list = []
        if value != "":
            detail_imgs = value.split(",")
            for detail_img in detail_imgs:
                detail_img_list.append(os.path.join(self.media_path, self.name, detail_img))
        self.__detailImages = detail_img_list

    @property
    def representativeImageUrl(self):  # getter
        return self.__representativeImageUrl

    @representativeImageUrl.setter
    def representativeImageUrl(self, value):  # setter
        self.__representativeImageUrl = value[0]

    @property
    def optionalImagesUrls(self):  # getter
        return self.__optionalImagesUrls

    @optionalImagesUrls.setter
    def optionalImagesUrls(self, value):  # setter

        option_img_url_list = []
        if value != []:
            for option_img_url in value:
                option_img_url_list.append({"url": option_img_url})

        self.__optionalImagesUrls = option_img_url_list

    @property
    def detailImagesUrls(self):  # getter
        return self.__detailImagesUrls

    @detailImagesUrls.setter
    def detailImagesUrls(self, value):  # setter
        self.__detailImagesUrls = value

    @property
    def detailContent(self):  # getter
        return self.__detailContent

    @detailContent.setter
    def detailContent(self, value):  # setter
        self.__detailContent = value

    @property
    def minorPurchasable(self):  # getter
        return self.__minorPurchasable

    @minorPurchasable.setter
    def minorPurchasable(self, value):  # setter
        self.__minorPurchasable = value

    @property
    def deliveryCompany(self):  # getter
        return self.__deliveryCompany

    @deliveryCompany.setter
    def deliveryCompany(self, value):  # setter
        self.__deliveryCompany = value

    @property
    def baseFee(self):  # getter
        return self.__baseFee

    @baseFee.setter
    def baseFee(self, value):  # setter
        self.__baseFee = value

    @property
    def sellerManagementCode(self):  # getter
        return self.__sellerManagementCode

    @sellerManagementCode.setter
    def sellerManagementCode(self, value):  # setter
        self.__sellerManagementCode = value

    @property
    def sellerTags(self):  # getter
        return self.__sellerTags

    @sellerTags.setter
    def sellerTags(self, value):  # setter
        self.__sellerTags = value

    # 옵션관련
    @property
    def have_option(self):  # getter
        return self.__have_option

    @have_option.setter
    def have_option(self, value):  # setter
        self.__have_option = value

    @property
    def optionGroupNames(self):  # getter
        return self.__optionGroupNames

    @optionGroupNames.setter
    def optionGroupNames(self, value):  # setter
        if value == "False":
            value = ""
        self.__optionGroupNames = value

    @property
    def optionNames(self):  # getter
        return self.__optionNames

    @optionNames.setter
    def optionNames(self, value):  # setter
        self.__optionNames = value

    @property
    def optionStockQuantity(self):  # getter
        return self.__optionStockQuantity

    @optionStockQuantity.setter
    def optionStockQuantity(self, value):  # setter
        self.__optionStockQuantity = value

    @property
    def optionPrices(self):  # getter
        return self.__optionPrices

    @optionPrices.setter
    def optionPrices(self, value):  # setter
        self.__optionPrices = value
