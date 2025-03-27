from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicia  driver
driver = webdriver.Chrome()  

# Abre la URL
driver.get("https://evolve-wp.com")

try:
    
    # Espera y selecciona el elemento de la nav con el id 'menu-item-122'
    menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "menu-item-122"))
    )
    menu_item.click()
    print("Click en el menú realizado con éxito.")

    # URL cambia después de hacer clic en el menú
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    print(f"Redirigido a: {driver.current_url}")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit() 
