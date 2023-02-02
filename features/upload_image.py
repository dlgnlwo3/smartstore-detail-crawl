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
from common.utils import global_log_append
from api.commerce_api_book import *
from api.image_upload import *
import time


class ImageUploader:
    def __init__(self, log_msg: pyqtSignal):
        self.log_msg = log_msg

    # 네이버 API 이미지 업로드
    def upload_img(self, img_list: list, client_id: str, client_secret: str):
        print("upload")
        cmBot = CommerceImageUploader(client_id, client_secret)
        uploaded_images = cmBot.multi_image_upload(img_list)
        return uploaded_images
