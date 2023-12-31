import os
from enum import Enum
from datetime import datetime
import json
from mimetypes import MimeTypes


COMPANY_NAME = "consolework"
PROGRAM_ID = "smartstore-detail-crawl"
APP_DATA_PATH = os.path.join(os.getenv("APPDATA"), COMPANY_NAME)
PROGRAM_PATH = os.path.join(APP_DATA_PATH, PROGRAM_ID)


# 프로그램이 실행되는 exe파일 경로
EXE_PATH = os.getcwd()

if os.path.isdir(APP_DATA_PATH) == False:
    os.mkdir(APP_DATA_PATH)


PROGRAM_PATH = os.path.join(APP_DATA_PATH, PROGRAM_ID)
if os.path.isdir(PROGRAM_PATH) == False:
    os.mkdir(PROGRAM_PATH)

OUTPUT_FOLDER_NAME = "output"
if not os.path.isdir(OUTPUT_FOLDER_NAME):
    os.mkdir(OUTPUT_FOLDER_NAME)


TODAY_OUTPUT_FOLDER = os.path.join(os.getcwd(), OUTPUT_FOLDER_NAME, datetime.today().strftime("%Y%m%d"))
if not os.path.isdir(TODAY_OUTPUT_FOLDER):
    os.mkdir(TODAY_OUTPUT_FOLDER)

# ------------- API 저장 파일 생성 ------------- #
API_SAVE_PATH = os.path.join(PROGRAM_PATH, f"{PROGRAM_ID}_api.txt")


def get_api_save_data():
    saved_data = None
    if os.path.isfile(API_SAVE_PATH):
        with open(API_SAVE_PATH, "r", encoding="utf-8") as f:
            saved_data = json.loads(f.read())
    return saved_data


def write_api_save_data(dict_save: dict):

    if os.path.isfile(API_SAVE_PATH):
        os.remove(API_SAVE_PATH)
        with open(API_SAVE_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps((dict_save)))
            f.close()
    else:
        with open(API_SAVE_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps((dict_save)))
            f.close()

    return dict_save


class APISaveFile(Enum):
    COMMERCEAPI_CLIENT_ID = "COMMERCEAPI_CLIENT_ID"
    COMMERCEAPI_CLIENT_SECRET = "COMMERCEAPI_CLIENT_SECRET"


# 저장데이터 없는 경우 초기화
if not get_api_save_data():
    write_api_save_data(
        {
            APISaveFile.COMMERCEAPI_CLIENT_ID.value: "",
            APISaveFile.COMMERCEAPI_CLIENT_SECRET.value: "",
        }
    )
# ------------- API 저장 파일 생성 종료 ------------- #


# ------------- 상품 등록 저장 파일 생성 ------------- #
UPLOADER_SAVE_PATH = os.path.join(PROGRAM_PATH, f"{PROGRAM_ID}_uploader.txt")


def get_uploader_save_data():
    saved_data = None
    if os.path.isfile(UPLOADER_SAVE_PATH):
        with open(UPLOADER_SAVE_PATH, "r", encoding="utf-8") as f:
            saved_data = json.loads(f.read())
    return saved_data


def write_uploader_save_data(dict_save: dict):

    if os.path.isfile(UPLOADER_SAVE_PATH):
        os.remove(UPLOADER_SAVE_PATH)
        with open(UPLOADER_SAVE_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps((dict_save)))
            f.close()
    else:
        with open(UPLOADER_SAVE_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps((dict_save)))
            f.close()

    return dict_save


class UploaderSaveFile(Enum):
    EXCEL_FILE_NAME = "EXCEL_FILE_NAME"
    MEDIA_PATH_NAME = "MEDIA_PATH_NAME"
    DETAIL_IMG_NAME = "DETAIL_IMG_NAME"


# 저장데이터 없는 경우 초기화
if not get_uploader_save_data():
    write_uploader_save_data(
        {
            UploaderSaveFile.EXCEL_FILE_NAME.value: "",
            UploaderSaveFile.MEDIA_PATH_NAME.value: "",
            UploaderSaveFile.DETAIL_IMG_NAME.value: "",
        }
    )
# ------------- 상품 등록 저장 파일 생성 종료 ------------- #


# ------------- 로그 파일 경로 생성 시작 ------------- #
LOG_FOLDER_NAME = "log"
LOG_FOLDER_PATH = os.path.join(PROGRAM_PATH, LOG_FOLDER_NAME)
if not os.path.isdir(LOG_FOLDER_PATH):
    os.mkdir(LOG_FOLDER_PATH)
# ------------- 로그 파일 경로 생성 종료 ------------- #
