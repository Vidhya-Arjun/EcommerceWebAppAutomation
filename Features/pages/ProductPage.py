import random

from Features.pages.BasePage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    shopping_cart_icon_xpath = "//a[@class='shopping_cart_link']"
    product_names_xpath = "//div[@class='inventory_item_name ']"
    add_to_cart_xpath = "//button[contains(@id,'add-to-cart')]"


    def cart_icon_is_vissible(self):
        return self.is_element_visible("shopping_cart_icon_xpath",self.shopping_cart_icon_xpath)


    def select_random_products(self, count):
        elements = self.get_elements("product_names_xpath",self.product_names_xpath)

        product_list = [el.text for el in elements]

        random.shuffle(product_list)
        print("product list", product_list)
        print(len(product_list))
        selected_products = product_list[:count]
        print(len(selected_products))
        return selected_products

