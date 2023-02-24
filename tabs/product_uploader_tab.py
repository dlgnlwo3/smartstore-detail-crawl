import sys
import warnings

warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import *
from dtos.gui_dto import GUIDto
from common.utils import *
from config import *
from threads.product_uploader_thread import ProductUploaderThread
from tabs.API_setting_tab import APISettingUI


class ProductUploaderUI(QWidget):

    # 초기화
    def __init__(self):
        print(f"UPLOADER_SAVE_PATH: {UPLOADER_SAVE_PATH}")
        self.saved_data = get_uploader_save_data()
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

        excel_file_name = self.excel_file_name.text()
        media_path_name = self.media_path_name.text()
        detail_img_name = self.detail_img_name.text()

        dict_save = {
            UploaderSaveFile.EXCEL_FILE_NAME.value: excel_file_name,
            UploaderSaveFile.MEDIA_PATH_NAME.value: media_path_name,
            UploaderSaveFile.DETAIL_IMG_NAME.value: detail_img_name,
        }

        question_msg = "저장하시겠습니까?"
        reply = QMessageBox.question(self, "상태 저장", question_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            write_uploader_save_data(dict_save)
            print(f"현재 상태를 저장했습니다.")

        else:
            print(f"저장 취소")

    # 작업 시작
    def start_button_clicked(self):
        print(f"start")

        API_setting_tab = APISettingUI()
        commerceAPI_client_id = API_setting_tab.saved_data[APISaveFile.COMMERCEAPI_CLIENT_ID.value]
        commerceAPI_client_secret = API_setting_tab.saved_data[APISaveFile.COMMERCEAPI_CLIENT_SECRET.value]

        if self.excel_file_name.text() == "":
            print(f"엑셀 파일을 선택해주세요.")
            QMessageBox.information(self, "작업 시작", f"엑셀 파일을 선택해주세요.")
            return

        if commerceAPI_client_id == "":
            print(f"API KEY를 입력해주세요")
            QMessageBox.information(self, "작업 시작", f"API KEY를 입력해주세요")
            return

        if commerceAPI_client_secret == "":
            print(f"API SECRET을 입력해주세요.")
            QMessageBox.information(self, "작업 시작", f"API SECRET을 입력해주세요.")
            return

        if self.media_path_name.text() == "":
            print(f"사진 폴더를 선택해주세요.")
            QMessageBox.information(self, "작업 시작", f"사진 폴더를 선택해주세요.")
            return

        if self.detail_img_name.text() == "":
            print(f"상세 이미지를 선택해주세요.")
            QMessageBox.information(self, "작업 시작", f"상세 이미지를 선택해주세요.")
            return

        self.guiDto = GUIDto()
        self.guiDto.excel_file = self.excel_file_name.text()
        self.guiDto.commerceAPI_client_id = commerceAPI_client_id
        self.guiDto.commerceAPI_client_secret = commerceAPI_client_secret
        self.guiDto.media_path = self.media_path_name.text()
        self.guiDto.detail_img = self.detail_img_name.text()
        self.guiDto.catalog_search = self.catalog_search.isChecked()

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

    # 상세 이미지 선택
    def detail_img_select_button_clicked(self):
        print(f"clicked")
        file_name = QFileDialog.getOpenFileName(self, "", "", "image file (*.jpg *.jpeg *.png)")

        if file_name[0] == "":
            print(f"선택된 파일이 없습니다.")
            self.log_append(f"선택된 파일이 없습니다.")
            return

        print(file_name[0])
        self.detail_img_name.setText(file_name[0])

    # 메인 UI
    def initUI(self):

        # 엑셀 그룹박스
        excel_groupbox = QGroupBox("엑셀 파일 선택")
        self.excel_file_name = QLineEdit(f"{self.saved_data[UploaderSaveFile.EXCEL_FILE_NAME.value]}")
        self.excel_file_name.setDisabled(True)
        self.excel_file_select_button = QPushButton("파일 선택")

        self.excel_file_select_button.clicked.connect(self.excel_file_select_button_clicked)

        excel_inner_layout = QHBoxLayout()
        excel_inner_layout.addWidget(self.excel_file_name)
        excel_inner_layout.addWidget(self.excel_file_select_button)
        excel_groupbox.setLayout(excel_inner_layout)

        # 이미지 폴더 그룹박스
        media_path_groupbox = QGroupBox(f"이미지 폴더 선택")
        self.media_path_name = QLineEdit(f"{self.saved_data[UploaderSaveFile.MEDIA_PATH_NAME.value]}")
        self.media_path_name.setDisabled(True)
        self.media_path_select_button = QPushButton("폴더 선택")

        self.media_path_select_button.clicked.connect(self.media_path_select_button_clicked)

        media_path_inner_layout = QHBoxLayout()
        media_path_inner_layout.addWidget(self.media_path_name)
        media_path_inner_layout.addWidget(self.media_path_select_button)
        media_path_groupbox.setLayout(media_path_inner_layout)

        # 상세 이미지 선택 그룹박스
        detail_img_groupbox = QGroupBox("상세 이미지 선택")
        self.detail_img_name = QLineEdit(f"{self.saved_data[UploaderSaveFile.DETAIL_IMG_NAME.value]}")
        self.detail_img_name.setDisabled(True)
        self.detail_img_select_button = QPushButton("파일 선택")

        self.detail_img_select_button.clicked.connect(self.detail_img_select_button_clicked)

        detail_img_inner_layout = QHBoxLayout()
        detail_img_inner_layout.addWidget(self.detail_img_name)
        detail_img_inner_layout.addWidget(self.detail_img_select_button)
        detail_img_groupbox.setLayout(detail_img_inner_layout)

        # 카탈로그 검색 기능
        catalog_search_groupbox = QGroupBox("카탈로그 검색")
        self.catalog_search_label = QLabel("카탈로그 검색")
        self.catalog_search = QCheckBox()

        catalog_search_inner_layout = QHBoxLayout()
        catalog_search_inner_layout.addWidget(self.catalog_search_label)
        catalog_search_inner_layout.addWidget(self.catalog_search)
        catalog_search_groupbox.setLayout(catalog_search_inner_layout)

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

        mid_layout = QVBoxLayout()
        mid_layout.addWidget(media_path_groupbox)
        mid_layout.addWidget(detail_img_groupbox)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(5)
        bottom_layout.addWidget(catalog_search_groupbox, 3)
        bottom_layout.addWidget(start_stop_groupbox, 3)

        log_layout = QHBoxLayout()
        log_layout.addWidget(log_groupbox)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(bottom_layout)
        layout.addLayout(log_layout)

        self.setLayout(layout)
