from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
driver = webdriver.Chrome()

# driver.get("https://google.com")

#time.sleep(15)

##Test iniciar sesion
driver.get("https://accounts.google.com/signin")
time.sleep(3)

##Igresa mail

email_input = driver.find_element(By.ID, "IdentifierId")
email_input.send_keys("tucorreo@Gmail.com")
email_input.send_keys(Keys.RETURN)

time.sleep(5)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("TuPass")
password_input.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()