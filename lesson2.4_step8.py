from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100')
    )

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()


    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()