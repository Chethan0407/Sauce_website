# Logout Page Object: This module contains the Page Object class for the Logout page.
# It provides methods to interact with elements on the Logout page, such as clicking the hamburger menu
# and then clicking the logout button.


from selenium.webdriver.common.by import By

from .basePage import BasePage




class Logout(BasePage):
    HAMBURGER_MENU = (By.ID, "react-burger-menu-btn" )
    LOGOUT = (By.LINK_TEXT, 'Logout')


    def click_Ham_and_logout_button(self):
        self.click(self.HAMBURGER_MENU)
        self.click((self.LOGOUT))