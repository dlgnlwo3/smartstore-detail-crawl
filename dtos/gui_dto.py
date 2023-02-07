if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class GUIDto:
    def __init__(self):
        # API setting
        self.__commerceAPI_client_id = ""
        self.__commerceAPI_client_secret = ""

        # product_crawler에 사용합니다.
        self.__store_url = ""
        self.__product_list_excel_file = ""

        # product_uploader에 사용합니다.
        self.__excel_file = ""
        self.__media_path = ""
        self.__detail_img = ""

    # API setting
    @property
    def commerceAPI_client_id(self):  # getter
        return self.__commerceAPI_client_id

    @commerceAPI_client_id.setter
    def commerceAPI_client_id(self, value):  # setter
        self.__commerceAPI_client_id = value

    @property
    def commerceAPI_client_secret(self):  # getter
        return self.__commerceAPI_client_secret

    @commerceAPI_client_secret.setter
    def commerceAPI_client_secret(self, value):  # setter
        self.__commerceAPI_client_secret = value

    # product_crawler
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

    # product_uploader

    @property
    def excel_file(self):  # getter
        return self.__excel_file

    @excel_file.setter
    def excel_file(self, value):  # setter
        self.__excel_file = value

    @property
    def media_path(self):  # getter
        return self.__media_path

    @media_path.setter
    def media_path(self, value):  # setter
        self.__media_path = value

    @property
    def detail_img(self):  # getter
        return self.__detail_img

    @detail_img.setter
    def detail_img(self, value):  # setter
        self.__detail_img = value
