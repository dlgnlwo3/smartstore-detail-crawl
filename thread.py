if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2
from tkinter import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dtos.gui_dto import *
from datetime import timedelta
import time
from timeit import default_timer as timer
from process.smartstore import *


# import debugpy


class ProductListSearchThread(QThread):

    log_msg = pyqtSignal(str)
    product_list_search_finished = pyqtSignal()

    # 호출 시점
    def __init__(self):
        super().__init__()

    # guiDto세팅
    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def run(self):
        try:
            # debugpy.debug_this_thread()

            self.log_msg.emit(f"검색 시작")

            start_time = timer()

            smartstoreCrawler = SmartStoreCrawler()

            smartstoreCrawler.setGuiDto(self.guiDto)

            smartstoreCrawler.get_all_product_urls()

            end_time = timer()

            progress_time = timedelta(seconds=end_time - start_time).seconds

            self.log_msg.emit(f"총 {str(progress_time)}초 소요되었습니다.")

        except Exception as e:
            print(f"작업 중 오류가 발생했습니다. {str(e)}")
            self.log_msg.emit(f"작업 중 오류가 발생했습니다. {str(e)}")

        self.product_list_search_finished.emit()

    def stop(self):
        try:
            self.terminate()
        except Exception as e:
            print(e)


class ProductDetailSearchThread(QThread):

    log_msg = pyqtSignal(str)
    product_detail_search_finished = pyqtSignal()

    # 호출 시점
    def __init__(self):
        super().__init__()

    # guiDto세팅
    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def run(self):
        try:
            # debugpy.debug_this_thread()

            self.log_msg.emit(f"검색 시작")

            start_time = timer()

            smartstoreCrawler = SmartStoreCrawler()

            smartstoreCrawler.setGuiDto(self.guiDto)

            smartstoreCrawler.setLogger(self.log_msg)

            smartstoreCrawler.work_start()

            end_time = timer()

            progress_time = timedelta(seconds=end_time - start_time).seconds

            self.log_msg.emit(f"총 {str(progress_time)}초 소요되었습니다.")

        except Exception as e:
            print(f"작업 중 오류가 발생했습니다. {str(e)}")
            self.log_msg.emit(f"작업 중 오류가 발생했습니다. {str(e)}")

        self.log_msg.emit(f"{smartstoreCrawler.i} / {smartstoreCrawler.row['상품명']} 상품까지 저장되었습니다.")

        self.product_detail_search_finished.emit()

    def stop(self):
        try:
            self.terminate()
        except Exception as e:
            print(e)
