
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.maximus.com.ar/LOGIN/login/maximus.aspx") 


username_input = driver.find_element(By.ID, "usuario")  
password_input = driver.find_element(By.ID, "clave")  
login_button = driver.find_element(By.NAME, "Login")

username_input.clear()
username_input.send_keys("mi_usuario") 

password_input.clear()
password_input.send_keys("mi_contraseña")


time.sleep(20)


print("Prueba exitosa: Login correcto.")



