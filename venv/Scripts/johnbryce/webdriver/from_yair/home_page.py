from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from my_wrapper import SeleniumWrapper


class HomePage(SeleniumWrapper):

    def click_on_nav_menu(self,nav_menu_title) -> bool:
        element = super().get_element_from_list_by_text_by_class("nav-li-Links", nav_menu_title)
        if element is not None:
            element.click()
            return True
        return False

    def mouse_hover_cart(self):
        cart = self.driver.find_element_by_id("menuCart")
        return super()._mouse_hover_element(cart)

    def is_tool_tip_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "toolTipCart")))
            return True
        except TimeoutException:
            # TODO: Add message to log when available
            return False

    # def get_cart_text(self):
    #     cart = self.driver.f
            # if title == "Special offers":
            #     nav_link.click()