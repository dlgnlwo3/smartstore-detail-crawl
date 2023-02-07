if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from common.chrome import *
from dtos.gui_dto import *
from common.utils import global_log_append
from tabs.product_crawler_tab import ProductCrawlerUI
from tabs.product_uploader_tab import ProductUploaderUI
from tabs.API_setting_tab import APISettingUI
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from config import *


# 오류 발생 시 프로그램 강제종료 방지
def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    global_log_append(str(value))
    sys._excepthook(exctype, value, traceback)


sys.excepthook = my_exception_hook

# pyinstaller -n "스마트스토어 v0.0.8 (openAPI 삭제 및 정리)" -w --onefile --clean "main.py" --icon "assets\smartstore.ico"


class MainUI(QWidget):
    # 초기화
    def __init__(self):
        print(f"PROGRAM_PATH: {PROGRAM_PATH}")
        print(f"EXE_PATH: {EXE_PATH}")

        # 로그 폴더
        self.log_path = os.path.join(os.getcwd(), "log")
        if os.path.isdir(self.log_path) == False:
            os.mkdir(self.log_path)
        else:
            print(f"{self.log_path} 이미 로그 폴더가 있습니다.")

        # UI
        super().__init__()
        self.initUI()

    # 가운데 정렬
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 프로그램 닫기 클릭 시
    def closeEvent(self, event):
        quit_msg = "프로그램을 종료하시겠습니까?"
        reply = QMessageBox.question(self, "프로그램 종료", quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print(f"프로그램을 종료합니다.")
            event.accept()
        else:
            print(f"종료 취소")
            event.ignore()

    # 아이콘 설정
    def set_window_icon_from_response(self, http_response):
        pixmap = QPixmap()
        pixmap.loadFromData(http_response.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)

    # 메인 UI
    def initUI(self):
        # 이미지 주소를 복사해야 함
        ICON_IMAGE_URL = "https://i.imgur.com/MyAplh0.png"
        self.icon = QNetworkAccessManager()
        self.icon.finished.connect(self.set_window_icon_from_response)
        self.icon.get(QNetworkRequest(QUrl(ICON_IMAGE_URL)))

        # 탭 초기화
        self.API_setting_tab = APISettingUI()
        self.product_crawler_tab = ProductCrawlerUI()
        self.product_uploader_tab = ProductUploaderUI()

        # 탭 추가
        tabs = QTabWidget()
        tabs.addTab(self.product_crawler_tab, "상품수집")
        tabs.addTab(self.product_uploader_tab, "상품등록")
        tabs.addTab(self.API_setting_tab, "API 설정")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)

        # 앱 기본 설정
        self.setWindowTitle("스마트스토어 v0.0.8")
        self.resize(600, 600)
        self.center()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(app.exec_())
