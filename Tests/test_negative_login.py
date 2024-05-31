import time

from selenium.common import NoSuchElementException

from Pages.loginPage import LoginPage
import pytest
from Tests.BaseTest import BaseTestPage
from Utilities.test_data import TestData

from Utilities.logger_config import configure_logger

logger = configure_logger()


@pytest.mark.usefixtures("driver")
class TestLogin(BaseTestPage):
    @pytest.mark.sanity
    def test_login_page(self, driver):
        uname = TestData.invalid_Uname
        password = TestData.Invalid_pass
        logger.info("Negative test login started")
        invalid_login = LoginPage(driver)
        invalid_login.do_login(uname, password)
        time.sleep(10)
        try:
            error_message = invalid_login.invalid_cred_message_verify()
        except NoSuchElementException:
            pytest.fail("element has not found")
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        assert error_message == expected_error_message, (f"Expected error message "
                                                         f"'{expected_error_message}' but got '{error_message}'")

        logger.info("Negative tests login ended")
