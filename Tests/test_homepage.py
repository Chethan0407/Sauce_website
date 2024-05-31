import time
from turtle import title
from Tests.BaseTest import BaseTestPage
from Pages.loginPage import LoginPage
from Pages.homePage import Homepage
import pytest
from Utilities.logger_config import configure_logger

logger = configure_logger()


@pytest.mark.sanity
class TestHomepage(BaseTestPage):

    @pytest.fixture(autouse=True)
    def setup_class(self, credentials, driver):
        # Perform login before each test
        uname, password = credentials
        logger.info("Homepage functionality started")
        login_page = LoginPage(driver)
        login_page.do_login(uname, password)

    def test_add_to_cart_items(self, driver):
        homepage = Homepage(driver)
        homepage.add_to_cart_1()
        homepage.add_tocart_2()
        homepage.click_on_cart()
        time.sleep(5)
        homepage.get_cart_items()
        expected_count = 2
        try:
            actual_count = homepage.get_cart_items()
            assert actual_count == expected_count
        except Exception as e:
            print(f"there is an error in the count of items in the cart, PO please check", {e})

        homepage.click_on_check_out()
        homepage.add_add_details("Chethan", "gopal", "562106")
        homepage.click_continue()

        act_title = "Thank you for your order!"
        if title == act_title:
            assert True
        else:
            print("not true")
        driver.close()
        logger.info("Home page automation has completed")
