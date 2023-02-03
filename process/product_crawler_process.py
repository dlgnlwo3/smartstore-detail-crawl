if 1 == 1:
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time
import pandas as pd
from common.chrome import *
import urllib.parse
from common.selenium_activities import *
from dtos.product_url_dto import *
from dtos.product_detail_dto import *
from dtos.gui_dto import GUIDto
from common.product_url_file import ProductURLFile
from common.utils import global_log_append
from config import TODAY_OUTPUT_FOLDER
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
import re


class ProductCrawlerProcess:
    def __init__(self):
        self.driver: webdriver.Chrome = get_chrome_driver_new(is_headless=False, is_scret=True)
        self.default_wait = 10
        self.driver.implicitly_wait(self.default_wait)
        self.current_count = 0
        self.worked_url_list = []

    def setGuiDto(self, guiDto: GUIDto):
        self.guiDto = guiDto

    def setLogger(self, log_msg):
        self.log_msg = log_msg

    def save_img_from_url(self, url: str, file_name: str, product_name: str):

        store_name = "store_name"
        try:
            store_name = self.guiDto.product_list_excel_file[
                self.guiDto.product_list_excel_file.rfind("/") + 1 : self.guiDto.product_list_excel_file.rfind("_상품목록")
            ]
        except Exception as e:
            pass

        image_path = os.path.join(TODAY_OUTPUT_FOLDER, store_name)
        print(image_path)
        if not os.path.isdir(image_path):
            os.mkdir(image_path)

        product_path = os.path.join(image_path, product_name)
        print(product_path)
        if not os.path.isdir(product_path):
            os.mkdir(product_path)

        file_name = os.path.join(product_path, file_name)
        try:
            urllib.request.urlretrieve(f"{url}", f"{file_name}")
        except Exception as e:
            print(f"{url} 이미지 생성 실패")
        time.sleep(0.2)

    def all_product_url_to_excel(self, products):
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        store_name = self.guiDto.store_url.split("/")[-1]
        product_excel = os.path.join(TODAY_OUTPUT_FOLDER, f"{store_name}_상품목록_{now}.xlsx")
        pd.DataFrame.from_dict(products).to_excel(product_excel, index=False)

    def product_detail_to_excel(self, products):
        store_name = self.guiDto.product_list_excel_file.split("_")[0]
        product_excel = os.path.join(TODAY_OUTPUT_FOLDER, f"{store_name}_상품상세정보.xlsx")
        pd.DataFrame.from_dict(products).to_excel(product_excel, index=False)

    # 모든 상품의 url 수집
    def get_all_product_urls(self):
        driver = self.driver

        product_url_list = []

        # 해당 스토어에 접속, 물품 80개씩 보기, 리스트 형식 정렬 및 누적판매순 정렬
        # ex) https://smartstore.naver.com/dokkaebistore/category/ALL?st=TOTALSALE&dt=LIST&page=1&size=80

        # 페이지를 넘기며 모든 물품의 url 수집
        current_page = 1
        while True:
            driver.get(f"{self.guiDto.store_url}/category/ALL?st=TOTALSALE&dt=LIST&page={current_page}&size=80")
            # 로딩대기
            WebDriverWait(driver, self.default_wait).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "a:lst.product")]'))
            )
            time.sleep(1)

            # 현재 url과 현재 페이지가 일치하지 않는 경우 조회 종료
            if f"page={current_page}" not in driver.current_url:
                print(f"url 조회 종료")
                break

            # 현재 페이지의 상품 url 수집
            product_links = driver.find_elements(By.XPATH, '//a[contains(@class, "a:lst.product")]')

            # 상품 url 저장
            for product_link in product_links:
                product_url_dto = ProductURLDto()
                product_url_dto.product_name = product_link.find_element(By.CSS_SELECTOR, "strong").get_attribute(
                    "textContent"
                )
                product_url_dto.product_url = product_link.get_attribute("href")
                print(f"{product_url_dto.product_name} {product_url_dto.product_url}")

                if re.search('[\/:*?"<>|]', product_url_dto.product_name) == None:
                    product_url_list.append(product_url_dto.get_dict())
                else:
                    print(f"파일명에 사용할 수 없는 특수문자 포함")

            current_page += 1

        # 데이터 저장
        self.all_product_url_to_excel(product_url_list)

        # 크롬 드라이버 종료
        self.driver.quit()

    # url 인코드
    def encode_url(self, url):
        encode_url = urllib.parse.unquote(url)
        print(encode_url)
        return encode_url

    # ProductDetailDto
    def get_product_detail_dto(self, product_name, product_url):
        product_detail_dto = ProductDetailDto()
        product_detail_dto.product_name = product_name
        product_detail_dto.product_url = product_url

        driver = self.driver

        # url로 이동
        driver.get(product_url)

        # 로딩대기
        WebDriverWait(driver, self.default_wait).until(
            EC.element_to_be_clickable((By.XPATH, '//a[./span[contains(text(), "구매하기")]]'))
        )
        time.sleep(1)

        # 카테고리
        try:
            categories = driver.find_elements(By.XPATH, '//a[last()][contains(@class, "a:ctt.cat")]')
            category = categories[-1].get_attribute("href").split("/")[-1]
            print(category)
            product_detail_dto.product_category = category
        except Exception as e:
            print("카테고리 오류")

        # 가격
        try:
            price = (
                driver.find_element(
                    By.XPATH, '//strong[./span[contains(text(), "상품 가격")] and ./span[contains(text(), "원")]]//span[2]'
                )
                .get_attribute("textContent")
                .replace(",", "")
            )
            print(price)
            product_detail_dto.product_price = price
        except Exception as e:
            pass

        # 택배사
        try:
            delivery_company = driver.find_element(
                By.XPATH, '//div[./span[contains(text(), "택배배송")]]//span[3]'
            ).get_attribute("textContent")
            print(delivery_company)
            product_detail_dto.delivery_company = delivery_company
        except Exception as e:
            pass

        # 배송비
        try:
            delivery_fee = driver.find_element(
                By.XPATH, '//div[./span[contains(text(), "택배배송")]]//span[2]'
            ).get_attribute("textContent")
            delivery_fee = re.sub(r"[^0-9]", "", delivery_fee)
            print(delivery_fee)
            product_detail_dto.delivery_fee = delivery_fee
            print()
        except Exception as e:
            pass

        # 메인이미지
        try:
            file_name = ""
            product_main_img = (
                driver.find_element(By.XPATH, '//img[contains(@alt, "추가이미지0")]').get_attribute("src").rsplit("?")[0]
            )
            product_main_img = self.encode_url(product_main_img)
            if product_main_img.find("shop-phinf.pstatic.net") <= -1:
                raise Exception(f"{product_main_img} 메인이미지 획득 실패")
            img_format = product_main_img[product_main_img.rfind(".") :]
            file_name = f"{product_detail_dto.product_name}_메인이미지{img_format}"
            self.save_img_from_url(
                url=product_main_img, file_name=file_name, product_name=product_detail_dto.product_name
            )
            print(f"main_img: {file_name}")
            product_detail_dto.product_main_img = file_name
        except Exception as e:
            print(e)
            print(f"메인이미지 오류")
        finally:
            product_detail_dto.product_main_img = file_name

        # 추가이미지
        try:
            product_optional_imgs = []
            driver.implicitly_wait(1)
            optional_imgs = driver.find_elements(
                By.XPATH, '//img[contains(@alt, "추가이미지") and not(contains(@alt, "0"))]'
            )
            for i, optional_img in enumerate(optional_imgs):
                optional_img = optional_img.get_attribute("src").rsplit("?")[0]
                optional_img = self.encode_url(optional_img)
                if optional_img.find("shop-phinf.pstatic.net") <= -1:
                    print(f"{optional_img} 추가이미지 획득 실패")
                    continue
                img_format = optional_img[optional_img.rfind(".") :]
                file_name = f"{product_detail_dto.product_name}_추가이미지_{i}{img_format}"
                self.save_img_from_url(
                    url=optional_img, file_name=file_name, product_name=product_detail_dto.product_name
                )
                product_optional_imgs.append(file_name)
            print(f"optional_imgs: {product_optional_imgs}")
        except Exception as e:
            print(e)
        finally:
            driver.implicitly_wait(self.default_wait)
            product_detail_dto.product_optional_imgs = product_optional_imgs

        # 옵션
        # a tag 클릭 시 옵션이 들어있는 ul tag가 나온다.
        # $x('//a[contains(@class, "a:pcs.opopen")]')
        try:
            option_group_names = []
            option_names = []
            option_prices = []
            option_name = ""

            driver.implicitly_wait(1)
            option_selector = driver.find_element(By.XPATH, '//a[contains(@class, "a:pcs.opopen")]')
            product_detail_dto.product_option = "O"
            print(f"옵션이 있습니다.")

            # 옵션의 개수를 파악합니다. -> 숨겨져있는 element가 하나씩 더 검색됨...
            option_selectors = driver.find_elements(By.XPATH, '//a[contains(@class, "a:pcs.opopen")]')
            option_len = int(len(option_selectors) / 2)
            print(option_len)

            option_selectors = option_selectors[:option_len]

            # 옵션 1개
            if option_len == 1:
                print(f"옵션 1개 입니다.")

                for option_selector in option_selectors:
                    print(option_selector.get_attribute("textContent"))
                    option_group_names.append(option_selector.get_attribute("textContent"))

                    # 옵션 클릭 (열기)
                    actions = ActionChains(driver).move_to_element(option_selector).click()
                    actions.perform()
                    print()

                    # $x('//ul[@role="listbox"]//li')
                    option_li_els = driver.find_elements(By.XPATH, '//ul[@role="listbox"]//li')
                    for option_li in option_li_els:

                        # 옵션이름
                        option_name = option_li.get_attribute("textContent")

                        # 옵션가격
                        option_price = "0"
                        try:
                            price_pattern = r"[\+]+\d+['원']"
                            option_price: str = re.findall(price_pattern, option_name)[0]
                            option_price = option_price.replace("+", "")
                            option_price = option_price.replace("원", "")
                        except Exception as e:
                            pass
                        print(option_price)

                        option_name = option_name.replace(f" (+{option_price}원)", "")
                        option_names.append(f"{option_name}")
                        print(option_name)

                        option_prices.append(f"{option_price}")

                        print(f"{option_names} {option_prices}")
                        print()

                    # 옵션 클릭 (닫기)
                    actions = ActionChains(driver).move_to_element(option_selector).click()
                    actions.perform()
                    print()

            # 옵션 2개
            elif option_len == 2:
                print(f"옵션 2개 입니다.")

                first_option_names = []

                for option_selector in option_selectors:
                    option_group_name = option_selector.get_attribute("textContent")
                    print(option_group_name)
                    option_group_names.append(option_selector.get_attribute("textContent"))

                print(option_group_names)
                print()

                # 첫번째 옵션 그룹 열기
                driver.find_element(
                    By.XPATH, f'//a[contains(@class, "a:pcs.opopen")][contains(text(), "{option_group_names[0]}")]'
                ).click()

                # $x('//ul[@role="listbox"]//li')
                first_option_li_els = driver.find_elements(By.XPATH, '//ul[@role="listbox"]//li')

                for first_option_li in first_option_li_els:
                    first_option_name = first_option_li.get_attribute("textContent")
                    print(first_option_name)
                    first_option_names.append(first_option_name)

                # 첫번째 옵션 그룹 닫기
                driver.find_element(
                    By.XPATH, f'//a[contains(@class, "a:pcs.opopen")][contains(text(), "{option_group_names[0]}")]'
                ).click()

                print(first_option_names)
                print()

                for first_option_name in first_option_names:
                    # 첫번째 옵션 그룹 열기
                    driver.find_element(
                        By.XPATH, f'//a[contains(@class, "a:pcs.opopen")][contains(text(), "{option_group_names[0]}")]'
                    ).click()

                    # 첫번째 옵션 이름 클릭 (블랙)
                    driver.find_element(
                        By.XPATH, f'//a[contains(@class, "N=a:pcs.opone")][contains(text(), "{first_option_name}")]'
                    ).click()

                    # 두번째 옵션 그룹 열기
                    driver.find_element(
                        By.XPATH, f'//a[contains(@class, "a:pcs.opopen")][contains(text(), "{option_group_names[1]}")]'
                    ).click()

                    # 두번째 옵션 이름 추출
                    second_option_li_els = driver.find_elements(By.XPATH, '//ul[@role="listbox"]//li')

                    for second_option_li in second_option_li_els:
                        second_option_name = second_option_li.get_attribute("textContent")

                        # 옵션가격
                        option_price = "0"
                        try:
                            price_pattern = r"[\+]+\d+['원']"
                            option_price: str = re.findall(price_pattern, second_option_name)[0]
                            option_price = option_price.replace("+", "")
                            option_price = option_price.replace("원", "")
                        except Exception as e:
                            pass
                        print(option_price)
                        option_prices.append(f"{option_price}")

                        # 옵션이름
                        second_option_name = second_option_name.replace(" (품절)", "")
                        second_option_name = second_option_name.replace(f" (+{option_price}원)", "")
                        print(f"{first_option_name},{second_option_name}")
                        option_names.append(f"{first_option_name},{second_option_name}")

                    # 두번째 옵션 그룹 닫기
                    driver.find_element(
                        By.XPATH, f'//a[contains(@class, "a:pcs.opopen")][contains(text(), "{option_group_names[1]}")]'
                    ).click()

                    print(option_prices)
                    print(option_names)
                    print()

            # 옵션 3개
            elif option_len == 3:
                print(f"옵션 3개 입니다.")
                pass

        except Exception as e:
            print(e)
            print("option error")
        finally:
            driver.implicitly_wait(self.default_wait)

            product_detail_dto.option_group_names = option_group_names
            product_detail_dto.option_names = option_names
            product_detail_dto.option_prices = option_prices
            print()

        # 상세이미지 -> 화면상에 나타나지 않으면 이미지 src가 비정상적으로 출력됨 -> 한번씩 화면에 비춰줘야 정상적인 이미지 주소가 나옴

        try:
            product_detail_imgs = []
            driver.implicitly_wait(1)
            detail_imgs = driver.find_elements(
                By.XPATH, '//div[@class="se-main-container"]//a[@data-linktype="img"]//img'
            )
            for i, detail_img in enumerate(detail_imgs):
                actions = ActionChains(driver).move_to_element(detail_img)
                actions.perform()
                detail_img = detail_img.get_attribute("src").rsplit("?")[0]
                detail_img = self.encode_url(detail_img)
                if detail_img.find("shop-phinf.pstatic.net") <= -1:
                    print(f"{detail_img} 상세이미지 획득 실패")
                    continue
                img_format = detail_img[detail_img.rfind(".") :]
                file_name = f"{product_detail_dto.product_name}_상세이미지_{i}{img_format}"
                self.save_img_from_url(
                    url=detail_img, file_name=file_name, product_name=product_detail_dto.product_name
                )
                product_detail_imgs.append(file_name)
            print(f"detail_imgs: {product_detail_imgs}")
        except Exception as e:
            print(e)
        finally:
            driver.implicitly_wait(self.default_wait)
            product_detail_dto.product_detail_imgs = product_detail_imgs

        return product_detail_dto

    # 상품URL이 들어있는 엑셀파일을 이용해서 상품 상세정보를 가져옵니다.
    def get_all_product_details(self, excel_file):

        product_url_file = ProductURLFile(excel_file)
        df_product_url = product_url_file.df_product_url
        print(df_product_url)

        productDetailDtos = []

        for self.i, self.row in df_product_url.iterrows():

            try:
                product_name = str(self.row["상품명"])
                product_url = str(self.row["상품URL"])

                print(f"{self.i} {product_name} {product_url}")
                product_detail_dto: ProductDetailDto = self.get_product_detail_dto(product_name, product_url)

                print(f"{product_detail_dto.product_name}")
                productDetailDtos.append(product_detail_dto.get_dict())
                self.product_detail_to_excel(productDetailDtos)
                time.sleep(1)

                print(f"{self.i} / {product_name} 저장")

                self.log_msg.emit(f"{self.i} / {product_name} 저장")

            except Exception as e:
                print(e)
                global_log_append(str(e))
                continue

        # self.product_detail_to_excel(productDetailDtos)

        print(f"{self.i} / {product_name} 상품까지 저장되었습니다.")

        global_log_append(f"{self.i} / {product_name} 상품까지 저장되었습니다.")

        time.sleep(1)

    # 작업 시작
    def work_start(self):

        print(self.guiDto.product_list_excel_file)

        if os.path.isfile(self.guiDto.product_list_excel_file):
            print(f"{self.guiDto.product_list_excel_file} 작업 시작")
            self.get_all_product_details(self.guiDto.product_list_excel_file)

        else:
            print(f"{self.guiDto.product_list_excel_file} 엑셀 파일 오류")
            global_log_append(f"{self.guiDto.product_list_excel_file} 엑셀 파일 오류")

        time.sleep(1)

        # 크롬드라이버 종료
        self.driver.quit()


if __name__ == "__main__":

    # 기준입력 - 특정해시태그 포함된 게시물
    # 해당 계정 팔로우 수가 일정 수 이상인 계정리스트

    guiDto = GUIDto()
    guiDto.store_url = "https://smartstore.naver.com/dokkaebistore"
    guiDto.product_list_excel_file = (
        r"D:\Consolework\smartstore-detail-crawl\output\20230130\dokkaebistore_20230130163909.xlsx"
    )

    ProductCrawlerProcess = ProductCrawlerProcess()
    ProductCrawlerProcess.setGuiDto(guiDto)
    # ProductCrawlerProcess.get_all_product_urls()
    # ProductCrawlerProcess.save_img_from_url("asdf", "asdf", product_name=product_detail_dto.product_name)
    ProductCrawlerProcess.work_start()