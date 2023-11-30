from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disabled-extensions')

driver_path = "C:/Cursos/bigData/selenium/chrome/chromedriver.exe"
driver = webdriver.Chrome(driver_path, chrome_options=options)

# driver.get('https://eltiempo.es')
driver.get('https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html')

# WebDriverWait(driver, 5) \
#     .until(EC.element_to_be_clickable((By.CLASS_NAME,
#                                        'mfp-close'.replace(
#                                            ' ', '.')))) \
#     .click()
try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'mfp-close'))
    ).click()
except TimeoutException:
    print("El elemento 'mfp-close' no está presente o no es clickeable.")

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                       'wb-fieldflowwb-auto-1wb-auto-23'.replace(
                                           ' ', '.')))) \
    .click()
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                       'wb-fieldflowwb-auto-1wb-auto-23'))) \
    .send_keys('Temporary residence (visiting, studying, working)')
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.CLASS_NAME,
                                       'pagedetails'.replace(
                                           ' ', '.')))) \
    .click()



WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                       'wb-fieldflowwb-auto-1wb-auto-48'.replace(
                                           ' ', '.')))) \
    .click()
# WebDriverWait(driver, 5) \
#     .until(EC.element_to_be_clickable((By.NAME,
#                                        'wb-fieldflowwb-auto-1wb-auto-23'))) \
#     .send_keys('Temporary residence (visiting, studying, working)')

# WebDriverWait(driver, 5) \
#     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
#                                        'i.poi.poi-city'))) \
#     .click()
#
# WebDriverWait(driver, 5) \
#     .until(EC.element_to_be_clickable((By.XPATH,
#                                        '/html/body/div[5]/main/div[4]/div/section[5]/section/div/article/section[1]/ul/li[2]/h2/a'))) \
#     .click()
#
# WebDriverWait(driver, 5) \
#     .until(EC.element_to_be_clickable((By.XPATH,
#                                        '/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul')))
#
# texto_columnas = driver.find_element_by_xpath('/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul')
# texto_columnas = texto_columnas.text
# tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]
#
# horas = list()
# temp = list()
# v_viento = list()
#
# for i in range(0, len(tiempo_hoy), 4):
#     horas.append(tiempo_hoy[i])
#     temp.append(tiempo_hoy[i + 1])
#     v_viento.append(tiempo_hoy[i + 2])
#
# df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Viento_kmxh': v_viento})
# print(df)
# df.to_csv('tiempo_hoy_Barcelona.csv', index=False)
# driver.close()
