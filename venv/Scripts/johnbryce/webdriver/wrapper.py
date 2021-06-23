from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumWrapper:
    driver: webdriver = None
    driver_wait: WebDriverWait = None

    def __init__(self, driver: webdriver, driver_wait: WebDriverWait):
        self.driver = driver
        self.driver_wait = driver_wait


    def get_element(self, by: By, value: str) -> WebElement:
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException as e:
            return None

    def wait_for_element(self, by: By, value: str):
        try:
            self.driver_wait.until(method=EC.presence_of_element_located((by, value)))
        except TimeoutException as toe:
            return None

    def click_on_element(self, element: WebElement):
        try:
            element.click()
        except ElementNotVisibleException as enve:
            return None
