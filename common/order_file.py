if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import os
import pandas as pd


class OrderFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.initData()

    def get_excel_data_type(self):
        return {
            "상품명": str,
            "상품URL": str,
            "카테고리": str,
            "할인전가격": str,
            "판매가": str,
            "택배사": str,
            "배송비": str,
            "메인이미지": str,
            "추가이미지": str,
            "상세이미지": str,
            "옵션": str,
            "옵션그룹": str,
            "옵션이름": str,
            "옵션가격": str,
        }

    def initData(self):
        self.filepath = os.path.normpath(self.filepath)
        self.filename = os.path.basename(self.filepath)

        columns = self.get_excel_data_type()
        try:
            self.df_order = pd.read_excel(self.filepath, converters=columns, keep_default_na="")
            self.df_order = self.df_order.loc[:, list(columns.keys())]
        except Exception as e:
            print(e)

    def output(self):
        print(self.df_order)
        # self.df_order.to_excel('df_order.xlsx', index=False)


if __name__ == "__main__":

    order_file = OrderFile(r"D:\Consolework\smartstore-detail-crawl\excels\dokkaebistore_상품상세정보.xlsx")
    order_file.output()
