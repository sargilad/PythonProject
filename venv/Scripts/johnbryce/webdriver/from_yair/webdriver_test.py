import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from my_wrapper import SeleniumWrapper

search_term = "נמייה"
driver = webdriver.Chrome()
driver.get("http:\\www.google.com")
wrapper = SeleniumWrapper(driver)
input_box = driver.find_element_by_name("q")
input_box.send_keys(search_term)

time.sleep(2)
search_results = driver.find_elements_by_class_name("sbct")
for search_result in search_results:
    search_result_text = search_result.text
    if  "נחש" in search_result_text:
        search_result.click()
        break

driver.find_element_by_css_selector("div[class='abc def']")
driver.find_element_by_css_selector("button[translate='ADD_TO_CART']")
search_results_title = driver.find_element_by_class_name("LC20lb")
if search_term in search_results_title.text:
    print("passed")
else:
    print("failed")
time.sleep(2)
start_time = round(time.time() * 1000)
title_by_xpath = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/a")
# /html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/a
#//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a
end_time = round(time.time() * 1000)
print("it took ", end_time - start_time, " milli sceonds to find the href by xpath")

start_time = round(time.time() * 1000)

search_results_titles = driver.find_elements_by_class_name("yuRUbf")
for search_results_title in search_results_titles:
    search_result_a_tag = search_results_title.find_element_by_tag_name("a")
    end_time = round(time.time() * 1000)
    print("it took ", end_time -start_time, " milli sceonds to find the href")
    print(search_result_a_tag.get_attribute("href"))
#LC20lb DKV0Md
# if feeling_lucky_button is not None:
#     print("The button text is: " + feeling_lucky_button.text)
#     feeling_lucky_button.click()


# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[2]
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[2]