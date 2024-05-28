from selenium.webdriver.common.by import By
from .basePage import BasePage


class Homepage(BasePage):

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART2 = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CLICK_ON_CART = (By.ID, "shopping_cart_container")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_DESCRIPTION = (By.CSS_SELECTOR, ".inventory_item_desc")
    CHECH_OUT = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")


    def add_to_cart_1(self):
        self.click(self.ADD_TO_CART)

    def add_tocart_2(self):
        self.click(self.ADD_TO_CART2)

    def click_on_cart(self):
        self.click(self.CLICK_ON_CART)

    def click_on_check_out(self):
        self.click(self.CHECH_OUT)

    def get_cart_items(self):
        cart_items = self.find_elements(self.CART_ITEMS)
        return len(cart_items)

    def add_add_details(self, fname, lname, pin):
        self.send_keys(self.FIRST_NAME, fname)
        self.send_keys(self.LAST_NAME, lname)
        self.send_keys(self.ZIP, pin)

    def click_continue(self):
        self.click(self.CONTINUE)
        self.click(self.FINISH_BUTTON)











