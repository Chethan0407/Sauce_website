from pytest_bdd import scenario, given, when, then
from Pages.loginPage import LoginPage
from  Utilities.read_config import read_configuration
import pytest
import allure
import time

@pytest.mark.usefixtures("driver")

class TestLogin():
    @allure.feature('Login Feature')
    @allure.story('User Login to sauce')



    def test_login(self, driver):
        Uname = read_configuration('Default', 'Uname')
        password = read_configuration('Default', 'Password')


        loginpage = LoginPage(driver)
        loginpage.enter_username(Uname)
        loginpage.enter_password(password)
        loginpage.click_login()

        time.sleep(10)





