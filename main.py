from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disabled-extensions')
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
completed = False

driver_path = "C:/Users/josue/Projects/python/chrome/chromedriver.exe"
driver: WebDriver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get('https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html')

try:
    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'mfp-close'))
    ).click()
except TimeoutException:
    print("El elemento 'mfp-close' no está presente o no es clickeable.")

select_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='wb-auto-6']//select[1]"))
)
select_obj = Select(select_element)
select_obj.select_by_visible_text("Temporary residence (visiting, studying, working)")
driver.save_screenshot("screenshot.png")

select_element2 = WebDriverWait(driver, 20).until(
     EC.element_to_be_clickable((By.XPATH, "//div[@id='wb-auto-6']//select[2]"))
)

select_obj2 = Select(select_element2)
select_obj2.select_by_visible_text("Work permit (from outside Canada)")

select_element3 = WebDriverWait(driver, 300).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='wb-auto-6']//select[3]"))
)
select_obj3 = Select(select_element3)
select_obj3.select_by_visible_text("Mexico")
completed = True
if completed:
    WebDriverWait(driver, 10) \
       .until(EC.element_to_be_clickable((By.CLASS_NAME,
                                          'btn btn-primary mrgn-bttm-md'.replace(
                                           ' ', '.')))) \
       .click()
time.sleep(10)
processing_time_element = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[3]/div[4]/div[3]/div/div[2]/p/span"))
)

print("span_element", processing_time_element.text)
driver.save_screenshot("screenshotfinal.png")
driver.quit()
