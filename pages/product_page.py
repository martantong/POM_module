from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def is_basket_price_correct(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text \
               == self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text, "Basket price is incorrect"

    def is_add_to_basket_message_displayed(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_ADD), "Add to basket message is not displayed"

    def is_item_name_correct(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME).text\
               == self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME).text, "Item name is incorrect"
