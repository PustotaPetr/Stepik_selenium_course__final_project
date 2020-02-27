from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_have_text_about_empty_basket(self):
        empty_basket_element = self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET_LABEL)
        assert 'Your basket is empty.' in empty_basket_element[0].text ,\
            "Basket not empty"


    def should_not_be_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM),\
            "Basket have product items"
