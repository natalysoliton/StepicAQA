from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    option1.send_keys("Ivan")

    option2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    option2.send_keys("Ivanov")

    option3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    option3.send_keys("Ivan@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    button.send_keys(os.getcwd() + "/file.txt")  # https://automated-testing.info/t/zagruzka-fajla-cherez-webdriver/3823


    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()
