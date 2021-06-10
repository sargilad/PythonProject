from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from wrapper import SeleniumWrapper

driver = webdriver.Chrome(executable_path="./resources/chromedriver.exe")
selenium_wrapper = SeleniumWrapper(driver, WebDriverWait(driver, 2))

url = "https://www.google.com"
driver.get(url)
print(url in driver.current_url)
web_element = selenium_wrapper.get_element(By.NAME, "q")

web_element.send_keys("blablabla" + Keys.ENTER)
elements = driver.find_elements(By.CLASS_NAME, "LC20lb")
for element in elements:
    print(element.text + "\n")

driver.quit()
