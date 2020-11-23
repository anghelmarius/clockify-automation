from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

data = {"email": "email", "password": "passwords"}

driver = webdriver.Chrome()
driver.get("https://clockify.me/tracker")
time.sleep(2)
print("I'm on clockify")
assert "Clockify" in driver.title
driver.find_element_by_xpath("/html/body/app-root/register-layout/div/div/div/div/div[2]/login/div/form/div/div/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(data["email"])
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(data["password"])
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
print("Google auth succesfully")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/form/autocomplete-input/div/input").send_keys(sys.argv[1])
print("Add description")
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/div/div/div/div/div/div").click()
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[1]/div/div/div/div/project-picker2/section/div[1]/div/input").send_keys(sys.argv[2])
time.sleep(2)
driver.find_element_by_link_text(sys.argv[2]).click()
print("Project added")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/modes-btns/div/div[1]/div/a/img").click()
driver.find_element_by_link_text("Manual").click()
print("Manual mod selected")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/div[2]/input-duration/input").clear()
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/div[2]/input-duration/input").send_keys(sys.argv[3])
print("Time added")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='layout-main']/tracker2/div/div/div/time-tracker-recorder/div/div/div/div[2]/div/div[3]/a[2]").click()
time.sleep(1)
driver.quit()
print("All done. Operation succed!")
