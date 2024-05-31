import time

from Pages.loginPage import LoginPage
import pytest

from Pages.logoutPage import Logout
from Tests.BaseTest import BaseTestPage
from Utilities.logger_config import configure_logger

logger = configure_logger()


@pytest.mark.usefixtures("driver")
class TestLogin(BaseTestPage):
    @pytest.mark.sanity
    def test_login_page(self, driver, credentials):
        # logger getting started

        Uname, password = credentials
        logger.info("Login functionality started")
        loginpage = LoginPage(driver)
        loginpage.do_login(Uname, password)


    @pytest.mark.sanity
    def test_logout(self, driver):
        logout = Logout(driver)
        logout.click_Ham_and_logout_button()
        logger.info("logout completed")
