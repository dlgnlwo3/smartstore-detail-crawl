if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import os
import pandas as pd


class ProductURLFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.initData()

    def get_excel_data_type(self):
        return {"상품명": str, "상품URL": str}

    def initData(self):
        self.filepath = os.path.normpath(self.filepath)
        self.filename = os.path.basename(self.filepath)

        columns = self.get_excel_data_type()
        try:
            self.df_product_url = pd.read_excel(self.filepath, converters=columns, keep_default_na="")
            self.df_product_url = self.df_product_url.loc[:, list(columns.keys())]
        except Exception as e:
            print(e)

    def output(self):
        print(self.df_product_url)


if __name__ == "__main__":

    order_file = ProductURLFile(r"D:\Consolework\smartstore-detail-crawl\output\20230130\도깨비상점_상품목록.xlsx")
    order_file.output()
