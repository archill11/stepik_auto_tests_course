from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = num2.text
    value = int(x1) + int(x2)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_visible_text(str(value))

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()