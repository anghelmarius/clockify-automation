from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

with open('./data.json') as f:
  data = json.load(f)

driver = webdriver.Chrome()
driver.get("https://clockify.me/tracker")
time.sleep(2)
print("I'm on clockify")
driver.find_element_by_xpath("/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(data["email"])
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(data["password"])
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
print("Google auth succesfully")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/form/autocomplete-input/div/input").send_keys("test automation")
print("Add description")
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/div/div/div/div/div/div").click()
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/div/div/div/project-picker2/section/div[1]/div/input").send_keys("strada")
time.sleep(2)
driver.find_element_by_link_text("strada").click()
print("Project added")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/modes-btns/div/div[1]/div/a/img").click()
driver.find_element_by_link_text("Manual").click()
print("Manual mod selected")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/div[2]/input-duration/input").clear()
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/div[2]/input-duration/input").send_keys(100)
print("Time added")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/div[3]/a[2]").click()
print("All done. Operation succed!")
