# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()

try:
    print('Перейти на https://sbis.ru/')
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(2)

    print('Перейти в раздел "Контакты"')
    contacts = driver.find_elements(By.CSS_SELECTOR, '.sbisru-MenuPopupTemplate__title')
    assert contacts[0].is_displayed(), 'Контакты не отображаются'
    contacts[0].click()
    sleep(2)

    print('Кликнуть по баннеру тензора')
    tensor_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Main-btn--abs')
    assert tensor_btn.is_displayed(), 'Баннер тензора не отображается'
    tensor_btn.click()
    sleep(2)

    print('Кликнуть на https://tensor.ru/')
    driver.get(tensor_site)
    sleep(2)

    print('Проверить, что есть блок новости "Сила в людях"')
    content = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    driver.execute_script("arguments[0].scrollIntoView(true);", content)
    content_title = content.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-title')
    assert content_title.text == 'Сила в людях', 'Блок сила в людях отсутствует'
    sleep(2)

    print('Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about')
    details = content.find_element(By.CSS_SELECTOR, '.tensor_ru-link')
    details.click()
    assert driver.current_url == tensor_about, 'Неверный адрес сайта'
    sleep(2)
finally:
    driver.quit()