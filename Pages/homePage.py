from selenium.webdriver.common.by import By
from .basePage import BasePage
import re


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
    FILTER_BUTTON = (By.CSS_SELECTOR, 'select.product_sort_container[data-test="product-sort-container"]')
    LOW_TO_HIGH = (By.XPATH, "//select[@class='product_sort_container']/option[3]")
    HOMEPAGE_ASSERTS = (By.CLASS_NAME, "inventory_item")

    def check_filter(self):
        self.click(self.FILTER_BUTTON)
        self.click(self.LOW_TO_HIGH)
        products = self.find_elements(self.HOMEPAGE_ASSERTS)
        assert len(products) >= 2, "ecpect at least two products to be displayed"

        first_product_price = self.extract_price_from_element(products[0])
        # Store first product price as an attribute
        second_product_price = self.extract_price_from_element(products[1])

        # Compare prices
        assert first_product_price < second_product_price, (
            f"Expected first product price (${first_product_price}) "
            f"to be lower than second product price (${second_product_price})"
        )

        print("Assertion passed: First product price is lower than the second one.")

    @classmethod
    def extract_price_from_element(cls, product_element):
        product_text = product_element.text
        price_str = re.search(r'\$\d+\.\d{2}', product_text)
        if price_str:
            return float(price_str.group(0).strip('$'))
        else:
            raise ValueError(f"Price not found or invalid format in element text: {product_text}")

    def add_to_cart_1(self):
        self.click(self.ADD_TO_CART)

    def add_to_cart2(self):
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
