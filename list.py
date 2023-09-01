import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    import math


    x_element = browser.find_element(By.CSS_SELECTOR,'#num1')
    x = int(x_element.text)

    y_element = browser.find_element(By.CSS_SELECTOR,'#num2')
    y = int(y_element.text)

    sum = x + y

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
