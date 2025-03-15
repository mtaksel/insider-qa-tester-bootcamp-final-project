from pages.cart_page import CartPage
from pages.filter_page import FilterPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestAmazonShopping(BaseTest):
    def test_amazon_shopping(self):

        # 1. Go to https://www.amazon.com.tr/
        home_page = HomePage(self.driver)
        # 2. Verify that you are on the home page
        self.assertEqual(self.base_url, home_page.get_current_url(), 'Amazon Home Page did not open')
        home_page.accept_cookies()
        # 3. Type 'samsung' in the search field at the top of the screen and perform search.
        home_page.type_search_in_the_search_bar()
        home_page.click_search_button()

        filter_page = FilterPage(self.driver)
        filter_page.scroll_down_one_time()
        # 4. Verify that there are results for Samsung on the page that appears.
        self.assertIn(home_page.search_object, filter_page.get_third_product_text(),
                      'Search object not seen in results')
        filter_page.scroll_down_two_time()
        # 5. Click on the 2nd page from the search results and verify that the 2nd page is currently displayed on the page that opens.
        filter_page.click_second_page_button()
        self.assertIn(filter_page.second_page_url, home_page.get_current_url(), 'You are not in 2nd Page')
        filter_page.click_on_third_product()

        product_page = ProductPage(self.driver)
        # 7. Verify that you are on the product page
        self.assertTrue(product_page.is_add_to_cart_present, 'You are not in Product Page')
        # 8. Add the product to the cart
        product_page.click_add_to_cart()
        # 9. Verify that the product has been added to the cart
        self.assertEqual(product_page.cart_msg, product_page.is_product_added(), 'Product was not added to the cart')
        # 10. Go to the cart page
        product_page.go_to_the_cart()

        cart_page = CartPage(self.driver)
        # 11. Verify that you are on the cart page and that the correct product has been added to the cart
        self.assertIn(cart_page.CART_TITLE, self.driver.title, 'You are not in Cart Page')
        self.assertIn(home_page.search_object, cart_page.first_product_in_cart().lower(), 'There is no product in Your Cart')
        # 12. Delete the product from the cart and verify that it has been deleted
        cart_page.click_on_remove_button()
        self.assertTrue(home_page.search_object in cart_page.is_product_removed_from_the_cart().lower() and
                        cart_page.REMOVED in cart_page.is_product_removed_from_the_cart().lower(),'Product was not removed from the cart')
        # 13. Return to the home page and verify that it is on the home page
        cart_page.click_home_page_logo()
        self.assertEqual(home_page.HOME_PAGE_NAV_URL, home_page.get_current_url(), 'You are not in Home page')