from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://profile-psi-topaz.vercel.app/")
time.sleep(3)

driver.quit()
