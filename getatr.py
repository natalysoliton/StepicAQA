from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # math.log((abs(12 * math.sin(int(47)))))
    # print(math.log((abs(12 * math.sin(int(47))))))
    # people_checked = people_radio.get_attribute("checked")
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute("valuex")
    # x = x_element
    y = calc(x)

    option0 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    option0.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
