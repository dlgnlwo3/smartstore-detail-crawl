if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


# 도서 DTO
class BookDto:
    def __init__(self):
        self.__isbn13 = ""  # ISBN-13
        self.__publishDay = ""  # 출간일 'yyyy-MM-dd'
        self.__publisher = ""  # 출판사
        self.__authors = ""  # 글작가
        self.__illustrators = ""  # 그림작가
        self.__translators = ""  # 번역자명

    @property
    def isbn13(self):  # getter
        return self.__isbn13

    @isbn13.setter
    def isbn13(self, value):  # setter
        self.__isbn13 = value

    @property
    def publishDay(self):  # getter
        return self.__publishDay

    @publishDay.setter
    def publishDay(self, value):  # setter
        self.__publishDay = value

    @property
    def publisher(self):  # getter
        return self.__publisher

    @publisher.setter
    def publisher(self, value):  # setter
        self.__publisher = value

    @property
    def authors(self):  # getter
        return self.__authors

    @authors.setter
    def authors(self, value):  # setter
        self.__authors = value

    @property
    def illustrators(self):  # getter
        return self.__illustrators

    @illustrators.setter
    def illustrators(self, value):  # setter
        self.__illustrators = value

    @property
    def translators(self):  # getter
        return self.__translators

    @translators.setter
    def translators(self, value):  # setter
        self.__translators = value
