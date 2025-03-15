from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.a-truncate-cut')
    CART_TITLE = 'Alışveriş Sepeti'
    REMOVED = 'kaldırıldı'
    REMOVED_PRODUCT = (By.CLASS_NAME, 'sc-list-item-removed-msg')
    REMOVE_BUTTON = (By.CSS_SELECTOR, "input[value='Sil']")
    HOME_PAGE_LOGO = (By.ID, 'nav-logo')

    # Returns the first product name in the cart page
    def first_product_in_cart(self):
        return self.find(*self.FIRST_PRODUCT).text

    # Returns the "product removed from cart" text in the cart page
    def is_product_removed_from_the_cart(self):
        return self.find(*self.REMOVED_PRODUCT).text

    # Clicks the remove button to remove product in the cart page
    def click_on_remove_button(self):
        self.click_element(*self.REMOVE_BUTTON)

    # Clicks the Amazon Logo on top left to navigate home page.
    def click_home_page_logo(self):
        self.click_element(*self.HOME_PAGE_LOGO)