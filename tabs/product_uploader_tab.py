import sys
import warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import *
import os
from dtos.gui_dto import GUIDto
from threads.product_uploader_thread import ProductUploaderThread
from common.utils import *
from config import *

# pyinstaller --onefile --noconsole -n "플레이오토 가격수정 1.0.7" --clean "main.py" --icon "assets\cancel.ico"


class ProductUploaderUI(QWidget):

    # 초기화
    def __init__(self):

        self.save_file = os.path.join(os.getcwd(), "save_file.txt")
        self.save_excel_file_name = ""
        self.save_client_id = ""
        self.save_client_secret = ""
        self.save_media_path_name = ""

        if os.path.isfile(self.save_file) == False:
            f = open(self.save_file, "w", encoding="UTF8")
        else:
            f = open(self.save_file, "r", encoding="UTF8")
            self.save_excel_file_name = f.readline().strip()
            self.save_client_id = f.readline().strip()
            self.save_client_secret = f.readline().strip()
            self.save_media_path_name = f.readline().strip()
        f.close()

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

        excel_file_name = self.excel_file_name.text()
        client_id = self.client_id.text()
        client_secret = self.client_secret.text()
        media_path_name = self.media_path_name.text()

        question_msg = "저장하시겠습니까?"
        reply = QMessageBox.question(self, "상태 저장", question_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                f = open(self.save_file, "w", encoding="UTF8")
                f.write(f"{excel_file_name}\n")
                f.write(f"{client_id}\n")
                f.write(f"{client_secret}\n")
                f.write(f"{media_path_name}\n")
                f.close()
                print(f"현재 상태를 저장했습니다.")
            except Exception as e:
                print(e)
        else:
            print(f"저장 취소")

    # 작업 시작
    def start_button_clicked(self):
        print(f"start")

        if self.excel_file_name.text() == "":
            print(f"엑셀 파일을 선택해주세요.")
            QMessageBox.information(self, "작업 시작", f"엑셀 파일을 선택해주세요.")
            return

        if self.client_id.text() == "":
            print(f"API KEY를 입력해주세요")
            QMessageBox.information(self, "작업 시작", f"API KEY를 입력해주세요")
            return

        if self.client_secret.text() == "":
            print(f"API SECRET을 입력해주세요.")
            QMessageBox.information(self, "작업 시작", f"API SECRET을 입력해주세요.")
            return

        if self.media_path_name.text() == "":
            print(f"사진 폴더를 선택해주세요.")
            QMessageBox.information(self, "작업 시작", f"사진 폴더를 선택해주세요.")
            return

        self.guiDto = GUIDto()
        self.guiDto.excel_file = self.excel_file_name.text()
        self.guiDto.client_id = self.client_id.text()
        self.guiDto.client_secret = self.client_secret.text()
        self.guiDto.media_path = self.media_path_name.text()

        self.store_thread = ProductUploaderThread()
        self.store_thread.log_msg.connect(self.log_append)
        self.store_thread.store_finished.connect(self.finished)
        self.store_thread.setGuiDto(self.guiDto)

        self.start_button.setDisabled(True)
        self.stop_button.setDisabled(False)
        self.store_thread.start()

    # 작업 중지
    def stop_button_clicked(self):
        print(f"stop")
        self.log_append(f"작업 중지")
        self.finished()

    @pyqtSlot()
    def finished(self):
        print(f"finished")
        self.log_append(f"작업 종료")
        self.store_thread.stop()
        self.start_button.setDisabled(False)
        self.stop_button.setDisabled(True)
        print(f"thread_is_running: {self.store_thread.isRunning()}")

    # 엑셀 파일 선택
    def excel_file_select_button_clicked(self):
        print(f"excel file select")
        file_name = QFileDialog.getOpenFileName(self, "", "", "excel file (*.xlsx)")

        if file_name[0] == "":
            print(f"선택된 파일이 없습니다.")
            self.log_append(f"선택된 파일이 없습니다.")
            return

        print(file_name[0])
        self.excel_file_name.setText(file_name[0])

    # 이미지 경로 선택
    def media_path_select_button_clicked(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder != "":
            self.media_path_name.setText(folder)
        else:
            self.log_append(f"선택된 폴더가 없습니다.")

    # 메인 UI
    def initUI(self):

        # 엑셀 그룹박스
        excel_groupbox = QGroupBox("엑셀 파일 선택")
        self.excel_file_name = QLineEdit(f"{self.save_excel_file_name}")
        self.excel_file_name.setDisabled(True)
        self.excel_file_select_button = QPushButton("파일 선택")

        self.excel_file_select_button.clicked.connect(self.excel_file_select_button_clicked)

        excel_inner_layout = QHBoxLayout()
        excel_inner_layout.addWidget(self.excel_file_name)
        excel_inner_layout.addWidget(self.excel_file_select_button)
        excel_groupbox.setLayout(excel_inner_layout)

        # 로그인 그룹박스
        login_groupbox = QGroupBox(f"네이버 커머스 API")
        # self.commerce_check = QCheckBox(f"네이버 커머스 ID")
        self.client_id_label = QLabel("API KEY")
        self.client_id = QLineEdit(f"{self.save_client_id}")
        self.client_secret_label = QLabel("API SECRET")
        self.client_secret = QLineEdit(f"{self.save_client_secret}")

        login_inner_layout = QVBoxLayout()
        # login_inner_layout.addWidget(self.commerce_check)
        login_inner_layout.addWidget(self.client_id_label)
        login_inner_layout.addWidget(self.client_id)
        login_inner_layout.addWidget(self.client_secret_label)
        login_inner_layout.addWidget(self.client_secret)
        login_groupbox.setLayout(login_inner_layout)

        # 옵션 그룹박스
        option_groupbox = QGroupBox(f"작동 옵션")
        self.media_path_name = QLineEdit(f"{self.save_media_path_name}")
        self.media_path_name.setDisabled(True)
        self.media_path_select_button = QPushButton("이미지 경로 선택")

        self.media_path_select_button.clicked.connect(self.media_path_select_button_clicked)

        option_inner_layout = QVBoxLayout()
        option_inner_layout.addWidget(self.media_path_name)
        option_inner_layout.addWidget(self.media_path_select_button)
        option_groupbox.setLayout(option_inner_layout)

        # 작동 그룹박스
        start_stop_groupbox = QGroupBox(f"작업 시작")
        self.save_button = QPushButton("저장")
        self.start_button = QPushButton("시작")
        self.stop_button = QPushButton("중지")
        self.stop_button.setDisabled(True)

        self.save_button.clicked.connect(self.save_button_clicked)
        self.start_button.clicked.connect(self.start_button_clicked)
        self.stop_button.clicked.connect(self.stop_button_clicked)

        start_stop_inner_layout = QHBoxLayout()
        start_stop_inner_layout.addWidget(self.save_button)
        start_stop_inner_layout.addWidget(self.start_button)
        start_stop_inner_layout.addWidget(self.stop_button)
        start_stop_groupbox.setLayout(start_stop_inner_layout)

        # 로그 그룹박스
        log_groupbox = QGroupBox("로그")
        self.browser = QTextBrowser()

        log_inner_layout = QHBoxLayout()
        log_inner_layout.addWidget(self.browser)
        log_groupbox.setLayout(log_inner_layout)

        # 레이아웃 배치
        top_layout = QVBoxLayout()
        top_layout.addWidget(excel_groupbox)

        mid_layout = QHBoxLayout()
        mid_layout.addWidget(login_groupbox, 5)
        mid_layout.addWidget(option_groupbox, 5)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(7)
        bottom_layout.addWidget(start_stop_groupbox, 3)

        log_layout = QHBoxLayout()
        log_layout.addWidget(log_groupbox)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(bottom_layout)
        layout.addLayout(log_layout)

        self.setLayout(layout)
