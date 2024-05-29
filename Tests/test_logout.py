import time
from turtle import title

from Tests.BaseTest import BaseTestPage
from Pages.loginPage import LoginPage
from Pages.homePage import Homepage
from Pages.logoutPage import Logout
import pytest


class Test_Logout(BaseTestPage):

    @pytest.fixture(autouse=True)
    def setup_class(cls, credentials, driver):
        # Perform login before each test
        Uname, password = credentials
        login_page = LoginPage(driver)
        login_page.do_login(Uname, password)

    @pytest.mark.sanity
    def test_logout(self, driver):
         logout = Logout(driver)
         logout.click_Ham_and_logout_button()