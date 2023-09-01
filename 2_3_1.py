from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR,'#input_value')
    x = x_element.text
    y = calc(x)

    option0 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    option0.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()
