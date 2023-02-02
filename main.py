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
from datetime import datetime
from common.chrome import *
from dtos.gui_dto import *
from common.utils import global_log_append
from thread import *
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

# 오류 발생 시 프로그램 강제종료 방지
def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    global_log_append(str(value))
    sys._excepthook(exctype, value, traceback)


sys.excepthook = my_exception_hook

# pyinstaller -n "스마트스토어 상품상세정보 크롤러 (옵션x)" -w --onefile --clean "main.py" --icon "assets\smartstore.ico"


class MainUI(QWidget):

    # 초기화
    def __init__(self):

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

    # 로그 작성
    @pyqtSlot(str)
    def log_append(self, text):
        today = str(datetime.now())[0:10]
        now = str(datetime.now())[0:-7]
        self.browser.append(f"[{now}] {str(text)}")
        global_log_append(text)

    # 상품목록 시작 클릭
    def product_list_search_start_button_clicked(self):
        print(f"product list search start clicked")

        if self.store_url.text() == "":
            print(f"주소가 입력되지 않았습니다.")
            self.log_append(f"주소가 입력되지 않았습니다.")
            return

        guiDto = GUIDto()
        guiDto.store_url = self.store_url.text()

        print(f"상품목록 검색을 시작합니다. {guiDto.store_url}")

        self.product_list_search_thread = ProductListSearchThread()
        self.product_list_search_thread.log_msg.connect(self.log_append)
        self.product_list_search_thread.product_list_search_finished.connect(self.product_list_search_finished)
        self.product_list_search_thread.setGuiDto(guiDto)

        self.product_list_search_start_button.setDisabled(True)
        self.product_list_search_stop_button.setDisabled(False)
        self.product_list_search_thread.start()

    # 상품목록 중지 클릭
    @pyqtSlot()
    def product_list_search_stop_button_clicked(self):
        print(f"product list search stop clicked")
        self.log_append(f"중지 클릭")
        self.product_list_search_finished()

    # 상품목록 작업 종료
    @pyqtSlot()
    def product_list_search_finished(self):
        print(f"product list search thread finished")
        self.log_append(f"검색 작업 종료")
        self.product_list_search_thread.stop()
        self.product_list_search_start_button.setDisabled(False)
        self.product_list_search_stop_button.setDisabled(True)
        print(f"thread_is_running: {self.product_list_search_thread.isRunning()}")

    # 상품상세정보 시작 클릭
    def product_detail_search_start_button_clicked(self):
        print(f"search start clicked")

        if self.product_list_excel_file.text() == "":
            print(f"선택된 파일이 없습니다.")
            self.log_append(f"선택된 파일이 없습니다.")
            return

        guiDto = GUIDto()
        guiDto.product_list_excel_file = self.product_list_excel_file.text()

        print(f"상품목록 검색을 시작합니다. {guiDto.product_list_excel_file}")

        self.product_detail_search_thread = ProductDetailSearchThread()
        self.product_detail_search_thread.log_msg.connect(self.log_append)
        self.product_detail_search_thread.product_detail_search_finished.connect(self.product_detail_search_finished)
        self.product_detail_search_thread.setGuiDto(guiDto)

        self.product_detail_search_start_button.setDisabled(True)
        self.product_detail_search_stop_button.setDisabled(False)
        self.product_detail_search_thread.start()

    # 상품상세정보 중지 클릭
    @pyqtSlot()
    def product_detail_search_stop_button_clicked(self):
        print(f"search stop clicked")
        self.log_append(f"중지 클릭")
        self.product_detail_search_finished()

    # 상품상세정보 작업 종료
    @pyqtSlot()
    def product_detail_search_finished(self):
        print(f"search thread finished")
        self.log_append(f"검색 작업 종료")
        self.product_detail_search_thread.stop()
        self.product_detail_search_start_button.setDisabled(False)
        self.product_detail_search_stop_button.setDisabled(True)
        print(f"thread_is_running: {self.product_detail_search_thread.isRunning()}")

    # 엑셀 파일 선택
    def product_list_excel_file_select_button_clicked(self):
        print(f"excel file select")
        file_name = QFileDialog.getOpenFileName(self, "", "", "excel file (*.xlsx)")

        if file_name[0] == "":
            print(f"선택된 파일이 없습니다.")
            self.log_append(f"선택된 파일이 없습니다.")
            return

        print(file_name[0])
        self.product_list_excel_file.setText(file_name[0])

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

        # 상품목록 그룹박스
        product_list_groupbox = QGroupBox("상품목록 크롤링")
        self.store_url_label = QLabel(f"상점주소")
        self.store_url = QLineEdit("https://smartstore.naver.com/dokkaebistore")
        self.product_list_search_start_button = QPushButton("검색시작")
        self.product_list_search_stop_button = QPushButton("중지")
        self.product_list_search_stop_button.setDisabled(True)

        self.product_list_search_start_button.clicked.connect(self.product_list_search_start_button_clicked)
        self.product_list_search_stop_button.clicked.connect(self.product_list_search_stop_button_clicked)

        product_list_inner_layout = QHBoxLayout()
        product_list_inner_layout.addWidget(self.store_url_label)
        product_list_inner_layout.addWidget(self.store_url)
        product_list_inner_layout.addWidget(self.product_list_search_start_button)
        product_list_inner_layout.addWidget(self.product_list_search_stop_button)
        product_list_groupbox.setLayout(product_list_inner_layout)

        # 상품상세정보 그룹박스
        product_detail_groupbox = QGroupBox("상품 목록 설정")
        self.product_list_excel_file_label = QLabel(f"엑셀 파일 선택")
        self.product_list_excel_file = QLineEdit("")
        self.product_list_excel_file.setDisabled(True)
        self.product_list_excel_file.setPlaceholderText("엑셀 파일 선택")
        self.product_list_excel_file_select_button = QPushButton("파일 선택")
        self.product_detail_search_start_button = QPushButton("검색시작")
        self.product_detail_search_stop_button = QPushButton("중지")
        self.product_detail_search_stop_button.setDisabled(True)

        self.product_list_excel_file_select_button.clicked.connect(self.product_list_excel_file_select_button_clicked)
        self.product_detail_search_start_button.clicked.connect(self.product_detail_search_start_button_clicked)
        self.product_detail_search_stop_button.clicked.connect(self.product_detail_search_stop_button_clicked)

        product_detail_inner_layout = QHBoxLayout()
        product_detail_inner_layout.addWidget(self.product_list_excel_file_label)
        product_detail_inner_layout.addWidget(self.product_list_excel_file)
        product_detail_inner_layout.addWidget(self.product_list_excel_file_select_button)
        product_detail_inner_layout.addWidget(self.product_detail_search_start_button)
        product_detail_inner_layout.addWidget(self.product_detail_search_stop_button)
        product_detail_groupbox.setLayout(product_detail_inner_layout)

        # 로그 그룹박스
        log_groupbox = QGroupBox("로그")
        self.browser = QTextBrowser()

        log_inner_layout = QHBoxLayout()
        log_inner_layout.addWidget(self.browser)
        log_groupbox.setLayout(log_inner_layout)

        # 레이아웃 배치
        top_layout = QVBoxLayout()
        top_layout.addWidget(product_list_groupbox)
        top_layout.addWidget(product_detail_groupbox)

        mid_layout = QHBoxLayout()

        log_layout = QVBoxLayout()
        log_layout.addWidget(log_groupbox)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(log_layout)

        self.setLayout(layout)

        # 앱 기본 설정
        self.setWindowTitle("스마트스토어 상품상세정보 크롤러")
        self.resize(600, 600)
        self.center()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(app.exec_())
