from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD_FIRST_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button.btn-primary[name = "registration_submit"]')


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    BLOCKS_AFTER_EDDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_PRODUCT_ADDED_IN_BASKET = (By.CSS_SELECTOR,
            "div#messages .alert.alert-safe.alert-noicon.alert-success.fade.in:first-child  .alertinner  strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_LABEL = (By.CSS_SELECTOR, "div#content_inner > p")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")
