from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        element.send_keys("some text")

    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла