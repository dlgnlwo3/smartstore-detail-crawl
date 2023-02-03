if 1 == 1:
    import sys
    import warnings
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    warnings.simplefilter("ignore", UserWarning)
    sys.coinit_flags = 2
from PyQt5.QtCore import pyqtSignal
from common.utils import global_log_append
from dtos.gui_dto import GUIDto

from dtos.common_dto import CommonDto
from common.order_file import OrderFile

from api.commerce_api import CommerceAPI
from api.image_upload import CommerceImageUploader
from features.get_dto_from_row import GetDtos
from features.get_product_dict import GetProductDict
import time


class ProductUploaderProcess:
    def __init__(self, log_msg: pyqtSignal):
        self.log_msg = log_msg

    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto
        self.client_id = self.guiDto.client_id
        self.client_secret = self.guiDto.client_secret
        self.excel_file = self.guiDto.excel_file
        self.media_path = self.guiDto.media_path

    def work_start(self):
        print(f"work_start")

        try:
            order_file = OrderFile(self.guiDto.excel_file)
            df_order = order_file.df_order

            self.imageUploader = CommerceImageUploader(self.client_id, self.client_secret)

            self.addBot = CommerceAPI(client_id=self.client_id, client_secret=self.client_secret)

            get_dtos = GetDtos(df_order, self.media_path)

            get_dtos.get_common_dto_list()

            commonDto: CommonDto
            for commonDto in get_dtos.common_dto_list:

                try:
                    # 1. 로컬의 이미지를 네이버에 업로드하고 url로 가져옵니다.
                    commonDto = self.convert_img_url(commonDto)

                    # 2. API 요청을 위해 commonDto의 정보로 API 요청 데이터를 만듭니다.
                    product = GetProductDict().get_product(commonDto)

                    # 3. 상품을 올립니다.
                    result, fail_reason = self.addBot.add_product(product)

                    print(f"{result} {fail_reason}")

                    if result == True:
                        self.log_msg.emit(f"{commonDto.name} 등록 성공")
                    else:
                        self.log_msg.emit(f"{commonDto.name} 등록 실패")
                        self.log_msg.emit(f"실패 사유: {fail_reason}")

                    time.sleep(1)

                except Exception as e:
                    print(str(e))
                    if str(e).find("No such file or directory") > -1:
                        self.log_msg.emit(f"{commonDto.name} 이미지 파일을 확인해주세요.")
                    else:
                        self.log_msg.emit(f"{commonDto.name} {e}")
                    continue

        except Exception as e:
            print(e)
            self.log_msg.emit(str(e))

    # 이미지 업로드
    def convert_img_url(self, commonDto: CommonDto):
        commonDto.representativeImageUrl = self.imageUploader.multi_image_upload([commonDto.representativeImage])
        commonDto.optionalImagesUrls = self.imageUploader.multi_image_upload(commonDto.optionalImages)
        commonDto.detailImagesUrls = self.imageUploader.multi_image_upload(commonDto.detailImages)

        return commonDto