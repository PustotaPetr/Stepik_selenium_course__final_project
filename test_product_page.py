import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium import webdriver
from .pages.basket_page import BasketPage
import time

link_single_test = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

link_parameter_list = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                  marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"  ]

@pytest.mark.parametrize('link', link_parameter_list)
def test_guest_can_add_product_to_basket_parametrize(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_busket()
    product_page.should_be_equal_price()
    product_page.should_be_equal_product_name()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_busket()
    product_page.should_be_equal_price()
    product_page.should_be_equal_product_name()

@pytest.mark.xfail(reason="test must fail")
@pytest.mark.absent_test
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = link_single_test
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_busket()
    product_page.should_not_see_success_message()


def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    link = link_single_test
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_busket()
    product_page.should_see_success_message()


@pytest.mark.absent_test
def test_guest_cant_see_success_message(browser):
    link = link_single_test
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_see_success_message()


@pytest.mark.xfail(reason="test must fail")
@pytest.mark.absent_test
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = link_single_test
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_busket()
    product_page.should_disappeare_success_message()


@pytest.mark.login_test
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.login_test
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = link_single_test
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.basket_test
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = link_single_test
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_item()
    basket_page.should_have_text_about_empty_basket()

@pytest.mark.user_basket_test
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        email = str(time.time()) + "@dotest.com"
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        browser = webdriver.Chrome()
        login_page = LoginPage(browser,link)
        login_page.open()
        login_page.register_new_user(email, 'zxdfrt678')
        login_page.should_be_authorized_user()
        return browser

    def test_user_cant_see_success_message(self, browser):
        link = link_single_test
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = link_single_test
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_busket()
        product_page.should_be_equal_price()
        product_page.should_be_equal_product_name()

