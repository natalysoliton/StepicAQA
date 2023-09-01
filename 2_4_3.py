from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


try:

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
  #  browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))

   # button.click()
    browser.find_element(By.ID, "book").click()

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    y = calc(x)

    option0 = browser.find_element(By.ID, 'answer')
    option0.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()
