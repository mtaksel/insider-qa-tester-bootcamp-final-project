from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID,'submit.add-to-cart')
    ADDED_TO_CART_TEXT_LOCATION = (By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    cart_msg = 'Sepete eklendi'
    CART_IMAGE = (By.ID, 'nav-cart')

    # Checks the visibility of the 'Add to Cart' button
    def is_add_to_cart_present(self):
        return self.find(*self.ADD_TO_CART)

    # Clicks the 'Add To Cart' button
    def click_add_to_cart(self):
        self.click_element(*self.ADD_TO_CART)

    # Clicks the 'Cart' icon on top right
    def go_to_the_cart(self):
        self.click_element(*self.CART_IMAGE)

    # Checks the visibility of the 'Added to Cart' text
    def is_product_added(self):
        return self.find(*self.ADDED_TO_CART_TEXT_LOCATION).text