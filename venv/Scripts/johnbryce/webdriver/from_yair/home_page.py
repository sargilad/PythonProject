from selenium.webdriver.common.by import By

from my_wrapper import SeleniumWrapper


class HomePage(SeleniumWrapper):

    def click_on_nav_menu(self,nav_menu_title) -> bool:
        element = super().get_element_from_list_by_text_by_class("nav-li-Links", nav_menu_title)
        if element is not None:
            element.click()
            return True
        return False
            # if title == "Special offers":
            #     nav_link.click()