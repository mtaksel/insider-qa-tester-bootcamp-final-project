from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FilterPage(BasePage):
    THIRD_PRODUCT = (By.XPATH, "(//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal'])[3]")
    SECOND_PAGE_BUTTON = (By.XPATH, "//a[@aria-label='2 sayfasına git']")
    second_page_url = 'page=2'

    # Scrolls the page twice
    def scroll_down_two_time(self):
        for i in range(2):
            self.driver.execute_script("window.scrollBy(0, 3850);")
            sleep(2)

    # Scrolls the page one time
    def scroll_down_one_time(self):
        for i in range(1):
            self.driver.execute_script("window.scrollBy(0, 800);")

    # Clicks the '2' button on bottom right to go second page of the search results page
    def click_second_page_button(self):
        self.driver.implicitly_wait(10)
        self.click_element(*self.SECOND_PAGE_BUTTON)

    # Returns the text of third product from search results page
    def get_third_product_text(self):
        return self.get_text(self.THIRD_PRODUCT).lower()

    # Clicks the third product in the search results page
    def click_on_third_product(self):
        self.click_element(*self.THIRD_PRODUCT)
