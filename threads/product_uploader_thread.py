if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2
from common.utils import global_log_append
from PyQt5.QtCore import pyqtSignal, QThread
from dtos.gui_dto import GUIDto
from process.product_uploader_process import ProductUploaderProcess

import debugpy


# store
class ProductUploaderThread(QThread):
    log_msg = pyqtSignal(str)
    store_finished = pyqtSignal()

    # 호출 시점
    def __init__(self):
        super().__init__()

    def setGuiDto(self, guiDto: GUIDto):
        print("set guiDto")
        self.guiDto = guiDto

    def run(self):
        debugpy.debug_this_thread()

        self.log_msg.emit(f"작업 시작")

        self.client_id = self.guiDto.client_id
        self.client_secret = self.guiDto.client_secret
        self.excel_file = self.guiDto.excel_file
        self.media_path = self.guiDto.media_path

        try:
            productUploaderProcess = ProductUploaderProcess(self.log_msg)

            productUploaderProcess.setGuiDto(self.guiDto)

            productUploaderProcess.work_start()

        except Exception as e:
            print(e)
            self.log_msg.emit(str(e))

        self.store_finished.emit()

    def stop(self):
        try:
            self.terminate()
        except Exception as e:
            print(e)
