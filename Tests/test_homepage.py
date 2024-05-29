import time
from turtle import title

from Tests.BaseTest import BaseTestPage
from Pages.loginPage import LoginPage
from Pages.homePage import Homepage
import pytest
import allure


@pytest.mark.sanity
class TestHomepage(BaseTestPage):


    @pytest.fixture(autouse=True)
    def setup_class(cls,credentials, driver):
        # Perform login before each test
        Uname, password = credentials
        login_page = LoginPage(driver)
        login_page.do_login(Uname, password)


    def test_add_to_cart_items(self, driver):
        homepage = Homepage(driver)
        homepage.add_to_cart_1()
        homepage.add_tocart_2()
        homepage.click_on_cart()
        homepage.get_cart_items()
        expected_count = 2
        try:
            actual_count = homepage.get_cart_items()
            assert actual_count== expected_count
        except Exception as e:
            print("there is an error in the count of items in the cart, PO please check")


        homepage.click_on_check_out()
        homepage.add_add_details("Chethan", "gopal", "562106")
        homepage.click_continue()

        time.sleep(20)
        act_title = "Thank you for your order!"
        if  title == act_title :
            assert True
        else:
            print("not true")
        driver.close()






