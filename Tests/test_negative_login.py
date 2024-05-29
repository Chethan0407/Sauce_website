import time
from turtle import title

from selenium.common import NoSuchElementException

from Pages.loginPage import LoginPage
import pytest
from Tests.BaseTest import BaseTestPage
from Utilities.test_data import TestData



@pytest.mark.usefixtures("driver")

class TestLogin(BaseTestPage):
    @pytest.mark.sanity
    def test_login_page(self, driver):
        Uname = TestData.invalid_Uname
        password = TestData.Invalid_pass

        INVALID_LOGIN = LoginPage(driver)
        INVALID_LOGIN.do_login(Uname,password)
        try:
            error_message = INVALID_LOGIN.invalid_cred_message_verify()
        except NoSuchElementException:
            pytest.fail("element has not found")
        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        assert error_message == expected_error_message, f"Expected error message '{expected_error_message}' but got '{error_message}'"











