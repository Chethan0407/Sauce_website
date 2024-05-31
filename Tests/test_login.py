import time

from Pages.loginPage import LoginPage
import pytest
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
        logger.info("Login functionality completed")

