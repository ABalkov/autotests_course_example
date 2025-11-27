# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep

download_dir = os.path.abspath('C:\\Users\\aa.balkov\\autotest_course\\Homework_11')
# Настройки для Chrome
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

sbis_site = 'https://saby.ru/sbis-to-saby'
driver = webdriver.Chrome(options=options)
file_name = 'saby-setup.exe'
file_path = os.path.join(download_dir, file_name)

try:
    print('Перейти на https://saby.ru/sbis-to-saby')
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(2)

    print('В Footer найти "Скачать СБИС"')
    download_link = driver.find_element(By.CSS_SELECTOR, '[href="/download"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", download_link)

    print('Перейти по ней')
    download_link.click()
    sleep(2)

    print('Скачать СБИС Плагин для вашей ОС в папку с данным тестом')
    download_file_wrapper = driver.find_element(By.CSS_SELECTOR, '[href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup.exe"]')
    download_file = download_file_wrapper.find_element(By.TAG_NAME, 'span')
    download_file.click()

    print('Убедиться, что плагин скачался')
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: os.path.exists(file_path))

    print('Вывести на печать размер скачанного файла в мегабайтах')
    size_bytes = os.path.getsize(file_path)
    size_mb = size_bytes / (1024 * 1024)
    print(f'Файл успешно скачан. Размер: {size_mb:.2f} МБ')


finally:
    driver.quit()