class ProductDetailDto:
    def __init__(self):
        self.__product_name = ""
        self.__product_url = ""
        self.__product_category = ""
        self.__product_price = ""
        self.__delivery_company = ""
        self.__delivery_fee = ""
        self.__product_main_img = ""
        self.__product_optional_imgs = []
        self.__product_detail_imgs = []

        # 옵션
        self.__product_option = ""
        self.__option_group_names = []
        self.__option_names = []
        self.__option_prices = []

    @property
    def product_name(self):  # getter
        return self.__product_name

    @product_name.setter
    def product_name(self, value: str):  # setter
        self.__product_name = value

    @property
    def product_url(self):  # getter
        return self.__product_url

    @product_url.setter
    def product_url(self, value: str):  # setter
        self.__product_url = value

    @property
    def product_category(self):  # getter
        return self.__product_category

    @product_category.setter
    def product_category(self, value: str):  # setter
        self.__product_category = value

    @property
    def product_price(self):  # getter
        return self.__product_price

    @product_price.setter
    def product_price(self, value: str):  # setter
        self.__product_price = value

    @property
    def delivery_company(self):  # getter
        return self.__delivery_company

    @delivery_company.setter
    def delivery_company(self, value: str):  # setter
        self.__delivery_company = value

    @property
    def delivery_fee(self):  # getter
        return self.__delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value: str):  # setter
        self.__delivery_fee = value

    @property
    def product_main_img(self):  # getter
        return self.__product_main_img

    @product_main_img.setter
    def product_main_img(self, value: str):  # setter
        self.__product_main_img = value

    @property
    def product_optional_imgs(self):  # getter
        return self.__product_optional_imgs

    @product_optional_imgs.setter
    def product_optional_imgs(self, value: str):  # setter
        self.__product_optional_imgs = value

    @property
    def product_detail_imgs(self):  # getter
        return self.__product_detail_imgs

    @product_detail_imgs.setter
    def product_detail_imgs(self, value: str):  # setter
        self.__product_detail_imgs = value

    @property
    def product_option(self):  # getter
        return self.__product_option

    @product_option.setter
    def product_option(self, value: str):  # setter
        self.__product_option = value

    @property
    def option_group_names(self):  # getter
        return self.__option_group_names

    @option_group_names.setter
    def option_group_names(self, value: list):  # setter

        list_to_str = ""
        if len(value) > 0:
            list_to_str = ";".join(value)
        if len(list_to_str) > 0:
            list_to_str += ";"

        self.__option_group_names = list_to_str

    @property
    def option_names(self):  # getter
        return self.__option_names

    @option_names.setter
    def option_names(self, value: list):  # setter

        list_to_str = ""
        if len(value) > 0:
            list_to_str = ";".join(value)
        if len(list_to_str) > 0:
            list_to_str += ";"

        self.__option_names = list_to_str

    @property
    def option_prices(self):  # getter
        return self.__option_prices

    @option_prices.setter
    def option_prices(self, value: list):  # setter

        list_to_str = ""
        if len(value) > 0:
            list_to_str = ";".join(value)
        if len(list_to_str) > 0:
            list_to_str += ";"

        self.__option_prices = list_to_str

    def to_print(self):
        print("상품명", self.product_name)
        print("상품URL", self.product_url)

    def get_dict(self) -> dict:
        return {
            "상품명": self.product_name,
            "상품URL": self.product_url,
            "카테고리": self.product_category,
            "가격": self.product_price,
            "택배사": self.delivery_company,
            "배송비": self.delivery_fee,
            "메인이미지": self.product_main_img,
            "추가이미지": self.product_optional_imgs,
            "상세이미지": self.product_detail_imgs,
            "옵션": self.product_option,
            "옵션그룹": self.option_group_names,
            "옵션이름": self.option_names,
            "옵션가격": self.option_prices,
        }
