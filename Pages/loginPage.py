from selenium.webdriver.common.by import By
from .basePage import BasePage


class LoginPage(BasePage):
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_CLICK = (By.ID, 'login-button')


    def enter_username(self, Uname):
        self.send_keys(self.USER_NAME, Uname)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_CLICK)





