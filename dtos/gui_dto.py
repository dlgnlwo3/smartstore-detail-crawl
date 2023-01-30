class GUIDto:
    def __init__(self):
        self.__store_url = ""
        self.__product_list_excel_file = ""

    @property
    def store_url(self):  # getter
        return self.__store_url

    @store_url.setter
    def store_url(self, value: str):  # setter
        self.__store_url = value

    @property
    def product_list_excel_file(self):  # getter
        return self.__product_list_excel_file

    @product_list_excel_file.setter
    def product_list_excel_file(self, value: str):  # setter
        self.__product_list_excel_file = value
