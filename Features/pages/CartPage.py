from selenium.webdriver.common.by import By

from Features.pages.BasePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    shopping_cart_container_id = "shopping_cart_container"
    cart_item_xpath = "//div[@class='cart_item']//a/div"
    item_names_xpath = "//div[@class='inventory_item_name ' and normalize-space() ='{}']"
    item_prices_xpath = ".//div[@class='inventory_item_price']"
    products_addition_xpath = "//div[@class='inventory_item_name ' and normalize-space() ='{}']/following::button"
    cart_count_xpath = "//span[@class='shopping_cart_badge']"

   # 🔹 Open cart
    def open_cart(self):
        self.click_element("shopping_cart_container_id",self.shopping_cart_container_id)

    # 🔹 Get product names from cart
    def get_cart_item_names(self):
        items = self.get_elements("cart_item_xpath", self.cart_item_xpath)
        return [item.text for item in items]



    def add_products_tocart(self, item_name):
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.click_element("add_to_cart_xpath", xpath)


    def get_cart_count(self):
        return self.retrieve_element_text("cart_count_xpath",self.cart_count_xpath)