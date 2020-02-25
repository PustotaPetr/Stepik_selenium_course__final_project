from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_busket(self):
        add_to_busket_button = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_busket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_equal_price(self):
        blocks_after_add_to_basket = self.browser.find_elements(
            *ProductPageLocators.BLOCKS_AFTER_EDDING)
        title_of_blocks_after_add = [element.text for element in blocks_after_add_to_basket]
        price_block = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        assert price_block.text in title_of_blocks_after_add,\
            f"Adding price doesn`t equal product price {price_block.text}"

    def should_be_equal_product_name(self):
        blocks_after_add_to_basket = self.browser.find_elements(
            *ProductPageLocators.BLOCKS_AFTER_EDDING)
        title_of_blocks_after_add = [element.text for element in blocks_after_add_to_basket]
        title_block = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE)
        assert title_block.text in title_of_blocks_after_add,\
            f"Adding product name not equal added product name - '{title_block.text}'"

    def should_not_see_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.NAME_PRODUCT_ADDED_IN_BASKET),\
            'Test user  see the name of added product'

    def should_see_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.NAME_PRODUCT_ADDED_IN_BASKET),\
            'Test user doesn`t see the name of added product'

    def should_disappeare_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.NAME_PRODUCT_ADDED_IN_BASKET),\
            'element doesn`t desappeare'
