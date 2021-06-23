import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from my_wrapper import SeleniumWrapper

plus_button_class_name = "plus"
cart_quantity_class_name = "roboto-regular"
add_to_cart_name = "save_to_cart"

class ProductPage(SeleniumWrapper):

    def increment_product(self, how_many: int,delay_between_clicks=0.2):
        # how many param: how many times we will click on the + button
        for i in range(how_many):
            time.sleep(delay_between_clicks)
            self.driver.find_element_by_class_name(plus_button_class_name).click()

    def validate_product_quantity(self, expected_quantity:int) -> bool:
        actual_quantity = int(self.driver.find_element_by_name("quantity").get_attribute("value"))
        return expected_quantity == actual_quantity

    def click_add_to_cart_button(self):
        self.driver.find_element_by_name(add_to_cart_name).click()

    def validate_quantity_in_cart(self,expected_quantity:int):
        element_text = self.get_element_from_list_by_text_by_class(cart_quantity_class_name,"Items").text
        actual_quantity = int(element_text.split("(")[1].split(" ")[0])
        return actual_quantity == expected_quantity

    def wait_for_cart_to_appear(self, time_to_wait_in_seconds):
        WebDriverWait(self.driver,time_to_wait_in_seconds).until(EC.visibility_of_element_located((By.ID,"checkOutPopUp")))

