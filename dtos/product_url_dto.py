class ProductURLDto:
    def __init__(self):
        self.__product_name = ""
        self.__product_url = ""

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

    def to_print(self):
        print("상품명", self.product_name)
        print("상품URL", self.product_url)

    def get_dict(self) -> dict:
        return {"상품명": self.product_name, "상품URL": self.product_url}
