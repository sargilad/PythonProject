from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class SeleniumWrapper:
    driver: WebDriver

    def __init__(self, driver):
        self.driver: webdriver = driver

    def get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException as e:
            return None

    def get_element_from_list_by_text(self, locator: By, locator_value, text_to_search: str) -> WebElement:
        element_list = self.driver.find_elements(locator, locator_value)
        for element in element_list:
            element_text = element.text
            print(element_text)
            if text_to_search in element_text:
                return element
        return None

    def get_element_from_list_by_text_by_class(self, class_text, text_to_search):
        return self.get_element_from_list_by_text(By.CLASS_NAME, class_text, text_to_search)

    def get_element_from_list_by_text_by_id(self, resource_id, text_to_search):
        return self.get_element_from_list_by_text(By.ID, resource_id, text_to_search)

    def validate_title_exists(self):
        return len(self.driver.title) > 0

    def validate_page_title(self, expected_title):
        actual_title = self.driver.title
        return actual_title == expected_title

    def get_element_parent(self, element: WebElement) -> WebElement:
        return element.find_element_by_xpath("../")
