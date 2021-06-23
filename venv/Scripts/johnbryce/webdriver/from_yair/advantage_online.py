import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from home_page import HomePage
from product_page import  ProductPage
i = 9
print(i)
driver = webdriver.Chrome()
product_page = ProductPage(driver)
home_page = HomePage(driver)

driver.get("http://advantageonlineshopping.com/#/")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "speakersImg")))


speakers_element = driver.find_element_by_id("speakersImg")
speakers_y = speakers_element.location['y']
speakers_x = speakers_element.location['x']
speakers_height = speakers_element.size['height']
speakers_width = speakers_element.size['width']
print("Speaker y: ", speakers_y)
laptops_element = driver.find_element_by_id("laptopsImg")
laptops_y = laptops_element.location['y']
print("Laptop y: ", laptops_y)
if speakers_y + speakers_height == laptops_y:
     print("Height between lines was correct")

tablets_element = driver.find_element_by_id("tabletsImg")
tablets_x = tablets_element.location['x']

if speakers_x + speakers_width == tablets_x:
     print("Width between columns was correct")

headphones_element = driver.find_element_by_id("headphonesImg")
headphones_y = headphones_element.location['y']
headphones_height = headphones_element.size['height']

if speakers_y + (speakers_height*2) == headphones_y + headphones_height:
     print("Yeah!!")

initial_handle = driver.current_window_handle
print("current window handle before " + initial_handle)
window_handles = driver.window_handles
print("The window handles size before click ", len(window_handles))

print("Screen size is " , driver.get_window_size(initial_handle)['height'])
driver.maximize_window()
print("Screen size is after max " , driver.get_window_size(initial_handle)['height'])


facebook_icon = driver.find_element_by_name("follow_facebook")
facebook_icon_y = facebook_icon.location['y']
print("facebook y before " , facebook_icon_y)
actions = ActionChains(driver)
time.sleep(1)
actions.move_to_element(facebook_icon)\
     .perform()

facebook_icon_y = facebook_icon.location['y']
print("facebook y after " , facebook_icon_y)

facebook_icon.click()

home_page.switch_to_last_opened_tab()
print("current window handle after " + driver.current_window_handle)
print("The window handles size after click ", len(window_handles))

# driver.get("http://advantageonlineshopping.com/#/product/3")
# # elements = driver.find_elements_by_class_name("max-width")
# element = product_page.get_element_from_list_by_text_by_class("max-width", "PRODUCT SPECIFICATIONS")
# if element is not None:
#      print(element.text)
#
# how_many_clicks = 3
# product_page.increment_product(how_many_clicks,0.5)
# result = product_page.validate_product_quantity(how_many_clicks + 1)
# if not result:
#      print("Falied to validate quantity expected " , how_many_clicks + 1)
#
# product_page.click_add_to_cart_button()
# product_page.wait_for_cart_to_appear(3)
# product_page.validate_quantity_in_cart(how_many_clicks + 1)



# expected_title = "Advantage Shopping"
# if not home_page.validate_page_title(expected_title):
#     print("Failed to validate page title " + expected_title)
#
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "miceImg")))
# home_page.click_on_nav_menu("SPECIAL OFFER")

# Wait for nav menu to appear
# run in loop and wait until our critrea
# get element attribute and wait until opacity  = 1