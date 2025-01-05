from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


##DEshabilitar GPU que me da problemas
chrome_options = Options()
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--headless")

service = Service("C:\SeleniumDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://profile-psi-topaz.vercel.app")

link_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Watch deploy"))
)


##Busca boton por texto link

expected_url = "https://bookstorefrontend-henna.vercel.app"
link_url = link_element.get_attribute("href")

link_element.click()

WebDriverWait(driver, 10).until(EC.url_changes(link_url))

##URL actual a la que va
current_url = driver.current_url

##Condicional para comprobar si va 

url_esperada = "https://bookstorefrontend-henna.vercel.app"
if current_url == url_esperada:
    print("Prueba exitosa: El botón redirige correctamente.")
else:
    print(f"Error: La URL es {current_url}, pero se esperaba {url_esperada}.")
    
driver.quit()