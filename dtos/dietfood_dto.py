if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# 건강보조식품 DTO
class DietFoodDto:
    def __init__(self):
        self.__seoInfo = ""

    @property
    def seoInfo(self):  # getter
        return self.__seoInfo

    @seoInfo.setter
    def seoInfo(self, value):  # setter
        self.__seoInfo = value
