import time

from Features.pages.BasePage import BasePage
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    usernameinput_id = "user-name"
    passwordinput_id = "password"
    loginbutton_xpath = "//input[@id = 'login-button']"
    error_message_xpath ="//h3[@data-test='error']"
    hamburger_menu_button_xpath = "//button[@id='react-burger-menu-btn']"
    logoutbutton_xpath = "//nav[@class='bm-item-list']/a[@id='logout_sidebar_link']"
    product_title_xpath = "//span[@class='title' and normalize-space()='Products']"

    Bag_img_xpath = "//img[@class='inventory_item_img']/parent::a[@id='item_4_img_link']"
    go_back_button_xpath = "//button[contains(text(),'Back to products')]"

    def open_user_login_page(self):
        self.open_login_page()

    def enter_username(self, username):
        self.type_text("username_name", self.usernameinput_id, username)

    def enter_password(self, password):
        self.type_text("password_name", self.passwordinput_id, password)

    def click_login_btn(self):
        self.click_element("login_btn_xpath", self.loginbutton_xpath)


    def validate_login_result(self, result):
        if result == "dashboard":
            assert self.driver.current_url.__contains__("inventory"), "Dashboard not displayed"

        elif result == "error message":
            error_text = self.retrieve_element_text("error_message_xpath", self.error_message_xpath)
            assert error_text != "", "Error message not displayed"

    def click_logout_btn(self):
        self.click_element("hamburger_menu_button_xpath", self.hamburger_menu_button_xpath)
        self.click_element("logoutbutton_xpath", self.logoutbutton_xpath)