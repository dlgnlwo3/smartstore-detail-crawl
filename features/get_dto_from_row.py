from dtos.common_dto import CommonDto
from dtos.book_dto import BookDto
from dtos.dietfood_dto import DietFoodDto
import pandas as pd


class GetDtos:
    def __init__(self, df_order: pd.DataFrame, media_path: str):
        self.df_order = df_order
        self.media_path = media_path
        self.common_dto_list = []

    def get_common_dto_list(self):
        for i, row in self.df_order[:].iterrows():
            commonDto: CommonDto = self.get_common_dto_from_row_data(row)
            self.common_dto_list.append(commonDto)

    # CommonDto
    def get_common_dto_from_row_data(self, row: pd.Series):
        commonDto = CommonDto()
        commonDto.media_path = self.media_path
        commonDto.name = str(row["상품명"])
        commonDto.leafCategoryId = str(row["카테고리"])
        commonDto.before_discount_price = str(row["할인전가격"])
        commonDto.salePrice = str(row["판매가"])
        commonDto.stockQuantity = str(1)

        commonDto.representativeImage = str(row["메인이미지"])
        commonDto.optionalImages = str(row["추가이미지"])
        commonDto.detailImages = str(row["상세이미지"])

        commonDto.deliveryCompany = str(row["택배사"])
        commonDto.baseFee = str(row["배송비"])

        commonDto.have_option = str(row["옵션"])
        commonDto.optionGroupNames = str(row["옵션그룹"])
        commonDto.optionNames = str(row["옵션이름"])
        commonDto.optionStockQuantity = str(1)  # 옵션재고
        commonDto.optionPrices = str(row["옵션가격"])

        # 판매자 설정 코드
        commonDto.sellerManagementCode = str(row["상품URL"])

        return commonDto

    # DietFoodDto
    def get_dietfood_dto_from_row_data(self, row: pd.Series):
        dietfoodDto = DietFoodDto()
        dietfoodDto.seoInfo = str(row["검색설정"])
        return dietfoodDto

    # BookDto
    def get_book_dto_from_row_data(self, row: pd.Series):
        bookDto = BookDto()
        bookDto.isbn13 = str(row["ISBN-13"])
        bookDto.publishDay = str(row["출간일"])
        bookDto.publisher = str(row["출판사"])
        bookDto.authors = str(row["글작가"])
        bookDto.illustrators = str(row["그림작가"])
        bookDto.translators = str(row["번역자명"])
        return bookDto
