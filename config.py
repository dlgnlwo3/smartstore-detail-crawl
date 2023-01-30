import os
import shutil
from datetime import datetime

COMPANY_NAME = "consolework"
PROGRAM_ID = "playauto_excel"
APP_DATA_PATH = os.path.join(os.getenv("APPDATA"), COMPANY_NAME)

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
