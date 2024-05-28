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



    def do_login(self, Uname, password):
        self.send_keys(self.USER_NAME, Uname)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_CLICK)
        return Homepage(self.driver)








