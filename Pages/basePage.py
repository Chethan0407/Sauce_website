from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


# This file contains the BasePage class, which provides common methods for interacting with web elements.


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def clear(self, locator):
        self.find_elements(locator).clear()

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

    def element_is_visible(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator))


