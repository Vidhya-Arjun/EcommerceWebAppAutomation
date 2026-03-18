
from Features.pages.BasePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    shopping_cart_container_id = "shopping_cart_container"
    cart_item_xpath = "//div[@class='cart_item']"
    item_names_xpath = ".//div[@class='inventory_item_name']"
    item_prices_xpath = ".//div[@class='inventory_item_price']"

   # 🔹 Open cart
    def open_cart(self):
        self.click_element("shopping_cart_container_id",self.shopping_cart_container_id)
    # 🔹 Get all cart items
    def get_cart_items(self):
        return self.get_elements("cart_item_xpath",self.cart_item_xpath)

    # 🔹 Get product names from cart
    def get_cart_item_names(self):
        items = self.get_cart_items()
        return [item.self.get_elements("item_names_xpath",self.item_names_xpath).text for item in items]

    # 🔹 Get product prices from cart
    def get_cart_item_prices(self):
        items = self.get_cart_items()
        return [item.self.get_elements("item_prices_xpath",self.item_prices_xpath).text for item in items]