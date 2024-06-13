from selenium.webdriver.common.by import By

from Utilities.read_config import read_configuration
from .basePage import BasePage
from Pages.homePage import Homepage


class LoginPage(BasePage):
    Uname = read_configuration('Default', 'Uname')
    password = read_configuration('Default', 'Password')
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_CLICK = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def do_login(self, uname, password):
        self.send_keys(self.USER_NAME, uname)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_CLICK)
        return Homepage(self.driver)

    def invalid_cred_message_verify(self):
        error_message_element = self.find_element(self.ERROR_MESSAGE)

        return error_message_element.text
