from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service =service )
driver.get("https://google.com")

#if there's a situation where due to slow internet speed
#there's problem in loading the page, it may raise error
#that couldn't find the element, so this makes it wait for 5 seconds , then check
#if the element is there else kill /quit
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element =driver.find_element(By.CLASS_NAME, "gLFyf")#find search bar in chrome
input_element.clear()
input_element.send_keys("tech with tim!"+Keys.ENTER)
#or find_elements returns an array of elements that match
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Tech With Tim"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tech With Tim")
link.click()#LINK_TEXT checks for exact text
#PARTIAL_LINK_TEXT checks in a anchor tag or part of sth

time.sleep(10)
driver.quit()
