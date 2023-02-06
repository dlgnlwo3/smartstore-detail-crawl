import sys
import warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import *
import os

from threads.product_crawler_thread import ProductDetailSearchThread, ProductListSearchThread
from dtos.gui_dto import GUIDto
from common.utils import *
from config import *


class APISettingUI(QWidget):

    # 초기화
    def __init__(self):
        print(f"API_SAVE_PATH: {API_SAVE_PATH}")
        self.saved_data = get_api_save_data()
        print(self.saved_data)

        super().__init__()
        self.initUI()

    # 로그 작성
    @pyqtSlot(str)
    def log_append(self, text):
        today = str(datetime.now())[0:10]
        now = str(datetime.now())[0:-7]
        self.browser.append(f"[{now}] {str(text)}")
        global_log_append(text)

    # 상태 저장
    def save_button_clicked(self):

        openAPI_client_id = self.openAPI_client_id.text()
        openAPI_client_secret = self.openAPI_client_secret.text()
        commerceAPI_client_id = self.commerceAPI_client_id.text()
        commerceAPI_client_secret = self.commerceAPI_client_secret.text()

        dict_save = {
            SaveFile.OPENAPI_CLIENT_ID.value: openAPI_client_id,
            SaveFile.OPENAPI_CLIENT_SECRET.value: openAPI_client_secret,
            SaveFile.COMMERCEAPI_CLIENT_ID.value: commerceAPI_client_id,
            SaveFile.COMMERCEAPI_CLIENT_SECRET.value: commerceAPI_client_secret,
        }

        question_msg = "저장하시겠습니까?"
        reply = QMessageBox.question(self, "상태 저장", question_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            write_api_save_data(dict_save)
            print(f"현재 상태를 저장했습니다.")
        else:
            print(f"저장 취소")

    # 메인 UI
    def initUI(self):

        # 상품목록 그룹박스
        openAPI_groupbox = QGroupBox("네이버 오픈 API")
        self.openAPI_client_id_label = QLabel("API KEY")
        self.openAPI_client_id = QLineEdit(f"{self.saved_data[SaveFile.OPENAPI_CLIENT_ID.value]}")
        self.openAPI_client_secret_label = QLabel("API SECRET")
        self.openAPI_client_secret = QLineEdit(f"{self.saved_data[SaveFile.OPENAPI_CLIENT_SECRET.value]}")

        openAPI_inner_layout = QHBoxLayout()
        openAPI_inner_layout.addWidget(self.openAPI_client_id_label)
        openAPI_inner_layout.addWidget(self.openAPI_client_id)
        openAPI_inner_layout.addWidget(self.openAPI_client_secret_label)
        openAPI_inner_layout.addWidget(self.openAPI_client_secret)
        openAPI_groupbox.setLayout(openAPI_inner_layout)

        # 상품상세정보 그룹박스
        commerceAPI_groupbox = QGroupBox("네이버 커머스 API")
        self.commerceAPI_client_id_label = QLabel("API KEY")
        self.commerceAPI_client_id = QLineEdit(f"{self.saved_data[SaveFile.COMMERCEAPI_CLIENT_ID.value]}")
        self.commerceAPI_client_secret_label = QLabel("API SECRET")
        self.commerceAPI_client_secret = QLineEdit(f"{self.saved_data[SaveFile.COMMERCEAPI_CLIENT_SECRET.value]}")

        commerceAPI_inner_layout = QHBoxLayout()
        commerceAPI_inner_layout.addWidget(self.commerceAPI_client_id_label)
        commerceAPI_inner_layout.addWidget(self.commerceAPI_client_id)
        commerceAPI_inner_layout.addWidget(self.commerceAPI_client_secret_label)
        commerceAPI_inner_layout.addWidget(self.commerceAPI_client_secret)
        commerceAPI_groupbox.setLayout(commerceAPI_inner_layout)

        # 상태 저장 그룹박스
        save_groupbox = QGroupBox(f"작업 시작")
        self.save_button = QPushButton("저장")

        self.save_button.clicked.connect(self.save_button_clicked)

        save_inner_layout = QHBoxLayout()
        save_inner_layout.addWidget(self.save_button)
        save_groupbox.setLayout(save_inner_layout)

        # 로그 그룹박스
        log_groupbox = QGroupBox("로그")
        self.browser = QTextBrowser()

        log_inner_layout = QHBoxLayout()
        log_inner_layout.addWidget(self.browser)
        log_groupbox.setLayout(log_inner_layout)

        # 레이아웃 배치
        top_layout = QVBoxLayout()
        top_layout.addWidget(openAPI_groupbox)
        top_layout.addWidget(commerceAPI_groupbox)

        mid_layout = QHBoxLayout()
        mid_layout.addStretch(8)
        mid_layout.addWidget(save_groupbox, 2)

        log_layout = QVBoxLayout()
        log_layout.addWidget(log_groupbox)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(log_layout)

        self.setLayout(layout)
