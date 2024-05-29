from Pages.loginPage import LoginPage
import pytest
from Tests.BaseTest import BaseTestPage



@pytest.mark.usefixtures("driver")

class TestLogin(BaseTestPage):
    @pytest.mark.sanity
    def test_login_page(self, driver, credentials):
        Uname, password = credentials
        loginpage = LoginPage(driver)
        loginpage.do_login(Uname, password)








