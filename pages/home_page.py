from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ACCEPT_COOKIES = (By.ID, 'sp-cc-accept')
    search_object = 'samsung'
    HOME_PAGE_NAV_URL = 'https://www.amazon.com.tr/ref=nav_logo'

    # Accepts cookies
    def accept_cookies(self):
        self.click_element(*self.ACCEPT_COOKIES)

    # Locates search bar and types "samsuns" in search input
    def type_search_in_the_search_bar(self):
        self.find(*self.SEARCH_BAR).send_keys(self.search_object)

    # Clicks the search button on top right
    def click_search_button(self):
        self.click_element(*self.SEARCH_BUTTON)
