
from Tests.BaseTest import BaseTestPage
from Pages.loginPage import LoginPage
from Pages.logoutPage import Logout
import pytest
from Utilities.logger_config import configure_logger

logger = configure_logger()


class TestLogout(BaseTestPage):

    @pytest.fixture(autouse=True)
    def setup_class(self, credentials, driver):
        # Perform login before each test

        uname, password = credentials
        logger.info("login for logout functionality started")

        login_page = LoginPage(driver)
        login_page.do_login(uname, password)

    @pytest.mark.sanity
    def test_logout(self, driver):
        logout = Logout(driver)
        logout.click_Ham_and_logout_button()
        logger.info("logout completed")
