import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from product_page import  ProductPage

driver = webdriver.Chrome()
product_page = ProductPage(driver)
# driver.get("http://advantageonlineshopping.com/#/")
driver.get("http://advantageonlineshopping.com/#/product/3")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "max-width")))
# elements = driver.find_elements_by_class_name("max-width")
element = product_page.get_element_from_list_by_text_by_class("max-width", "PRODUCT SPECIFICATIONS")
if element is not None:
     print(element.text)

driver.find_element_by_css_selector("book[class='week abc']")

how_many_clicks = 3
product_page.increment_product(how_many_clicks,0.5)
result = product_page.validate_product_quantity(how_many_clicks + 1)
if not result:
     print("Falied to validate quantity expected " , how_many_clicks + 1)

product_page.click_add_to_cart_button()
product_page.wait_for_cart_to_appear(3)
product_page.validate_quantity_in_cart(how_many_clicks + 1)


# expected_title = "Advantage Shopping"
# if not home_page.validate_page_title(expected_title):
#     print("Failed to validate page title " + expected_title)
#
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "miceImg")))
# home_page.click_on_nav_menu("SPECIAL OFFER")

# Wait for nav menu to appear
# run in loop and wait until our critrea
# get element attribute and wait until opacity  = 1