from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

dataKeys = [
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Temporary residence (visiting, studying, working)',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Study permit (from outside Canada)',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Temporary residence (visiting, studying, working)',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Electronic Travel Authorization (eTA)',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Economic immigration',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Canadian Experience Class',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Economic immigration',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Skilled workers (Federal)',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Economic immigration',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Skilled trades (Federal)',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Citizenship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Citizenship grant',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Citizenship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Citizenship certificate (proof of citizenship)',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Citizenship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Resumption of citizenship',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Citizenship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Renunciation of citizenship',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Citizenship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Search of citizenship records',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Permanent resident cards',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Yes, I am renewing or replacing my card, or I sent a solemn declaration',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Permanent resident cards',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'No, I am waiting for my first card',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Replacing or amending documents, verifying status',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Verification of Status',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Replacing or amending documents, verifying status',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Replacement of valid temporary resident documents',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Replacing or amending documents, verifying status',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Amendments of immigration documents',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Replacing or amending documents, verifying status',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Amendments of valid temporary resident documents',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 2,
        'menuone': 'Temporary residence (visiting, studying, working)',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Study permit (from inside Canada)',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Economic immigration',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Provincial Nominees',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'Yes',
        'clickThree': "//div[@id='wb-auto-6']//select[3]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Economic immigration',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Provincial Nominees',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'No',
        'clickThree': "//div[@id='wb-auto-6']//select[3]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Family sponsorship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Spouse or common-law partner living inside Canada',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'In Quebec',
        'clickThree': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Family sponsorship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Spouse or common-law partner living inside Canada',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'Outside Quebec',
        'clickThree': "//div[@id='wb-auto-6']//select[3]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Family sponsorship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Spouse, common-law or conjugal partner living outside Canada',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'In Quebec',
        'clickThree': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Family sponsorship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Parents or grandparents',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'In Quebec',
        'clickThree': "//div[@id='wb-auto-6']//select[2]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
    {
        'responseSize': '1',
        'parts': 3,
        'menuone': 'Family sponsorship',
        'clickOne': "//div[@id='wb-auto-6']//select[1]",
        'menuTwo': 'Parents or grandparents',
        'clickTwo': "//div[@id='wb-auto-6']//select[2]",
        'menuThree': 'Outside Quebec',
        'clickThree': "//div[@id='wb-auto-6']//select[3]",
        'finalClick': 'btn btn-primary mrgn-bttm-md'
    },
]


def scrapping(dataKeys, arr):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disabled-extensions')
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')

    driver_path = "C:/Users/josue/Projects/python/chrome/chromedriver.exe"
    driver: WebDriver = webdriver.Chrome(driver_path, chrome_options=options)
    driver.get(
        'https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html')

    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'mfp-close'))
        ).click()
    except TimeoutException:
        print("El elemento 'mfp-close' no está presente o no es clickeable.")

        for item in dataKeys:
            completed = False
            select_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, item['clickOne']))
            )
            select_obj = Select(select_element)
            select_obj.select_by_visible_text(item['menuone'])

            select_element2 = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, item['clickTwo']))
            )

            select_obj2 = Select(select_element2)
            select_obj2.select_by_visible_text(item['menuTwo'])
            completed = True
            if item['parts'] == 2:
                WebDriverWait(driver, 10) \
                    .until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                       'btn btn-primary mrgn-bttm-md'.replace(
                                                           ' ', '.')))) \
                    .click()
                time.sleep(8)
                if item['menuTwo'] == 'Citizenship certificate (proof of citizenship)':
                    processing_time_element = WebDriverWait(driver, 2).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "/html/body/main/div[3]/div[4]/div[3]/div/p[3]/strong/span"))
                    )
                else:
                    processing_time_element = WebDriverWait(driver, 2).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "/html/body/main/div[3]/div[4]/div[3]/div/div[2]/p/span[2]"))
                    )
                obj = {item['menuTwo']: item['menuTwo'], 'result': processing_time_element.text}
                arr.append(obj)
            elif item['parts'] == 3:
                select_element3 = WebDriverWait(driver, 300).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@id='wb-auto-6']//select[3]"))
                )
                select_obj3 = Select(select_element3)
                select_obj3.select_by_visible_text(item['menuThree'])

                WebDriverWait(driver, 10) \
                    .until(EC.element_to_be_clickable((By.CLASS_NAME,
                                                       'btn btn-primary mrgn-bttm-md'.replace(
                                                           ' ', '.')))) \
                    .click()
                time.sleep(8)
                processing_time_element = WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/main/div[3]/div[4]/div[3]/div/div[2]/p/span[2]"))
                )
                obj = {item['menuThree']: item['menuThree'], 'result': processing_time_element.text}
                arr.append(obj)
    driver.quit()
    return arr


start_time = time.time()
arr = []
scrapping(dataKeys, arr)
for data in arr:
    print("data:", data)
end_time = time.time()
execution_time = end_time - start_time
print(f"El programa tomó {execution_time} segundos para ejecutarse.")
