from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://clockify.me/tracker")
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("anghel.narius123@gmail.com")
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("")
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/form/autocomplete-input/div/input").send_keys("test")
time.sleep(1)

