import pytest
from .pages.product_page import ProductPage

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
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/"\
    #    "the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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
