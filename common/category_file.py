if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import os
import pandas as pd


class CategoryFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.initData()

    def get_excel_data_type(self):
        return {
            "카테고리번호": str,
            "대분류": str,
            "중분류": str,
            "소분류": str,
            "세분류": str,
        }

    def initData(self):
        self.filepath = os.path.normpath(self.filepath)
        self.filename = os.path.basename(self.filepath)

        columns = self.get_excel_data_type()
        try:
            self.df_category = pd.read_excel(self.filepath, converters=columns, keep_default_na="")
            self.df_category = self.df_category.loc[:, list(columns.keys())]
        except Exception as e:
            print(e)

    def output(self):
        print(self.df_category)
        # self.df_category.to_excel('df_category.xlsx', index=False)


if __name__ == "__main__":

    category_file = CategoryFile(r"D:\Consolework\smartstore-detail-crawl\common\스마트스토어_카테고리코드.xls")
    category_file.output()
