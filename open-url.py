from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://nextjs-project-three-dun.vercel.app")

try:
    first_clickable = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-header"))
    )
    first_clickable.click()
    print("Este es un click en el primer card clickeable realizado con éxito.")
except Exception as e:
    print(f"Error al hacer clic: {e}")


time.sleep(10)

driver.quit()
