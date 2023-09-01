import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome()

class TestReg(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        print('setup executed')

    def tearDown(self) -> None:
        self.browser.quit()
        print('teardown executed')

    def test_reg1(self):

            browser.get("http://suninjuly.github.io/registration1.html")

            input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input3.send_keys("test@mail.ru")
            input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
            input4.send_keys("899993435")
            input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
            input5.send_keys("Moscow")
            button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
            button.click()

    def test_reg2(self):

            browser.get("http://suninjuly.github.io/registration2.html")

            input6 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']")
            input6.send_keys("Ivan")
            input7 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input7.send_keys("test@mail.ru")
            input8 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone']")
            input8.send_keys("899993435")
            input9 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address']")
            input9.send_keys("Moscow")
            buttn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
            buttn.click()

        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!")




if __name__ == "__main__":
    unittest.main()
