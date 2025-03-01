from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuracion de chrome sin ventanas
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")


# Configura ChromeDriver automáticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://profile-psi-topaz.vercel.app")

    # Esperar hasta que el enlace con texto "Watch backend" esté presente
    link_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Watch backend"))
    )

    # Hacer scroll hasta el enlace para evitar errores de visibilidad
    driver.execute_script("arguments[0].scrollIntoView();", link_element)

    # Esperar a que sea clickeable
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(link_element))

    # Obtener URL del enlace antes de hacer clic
    link_url = link_element.get_attribute("href")
    print(f"🔗 El botón apunta a: {link_url}")


    # Esperar cambio de URL
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

    # Obtener URL actual después del clic
    current_url = driver.current_url
    print(f"URL actual: {current_url}")

    # Verificar si la URL es la esperada
    expected_url = "https://github.com/ceurrutia/mylist"
    if current_url == expected_url:
        print("Prueba exitosa: El botón redirige correctamente.")
    else:
        print(f"Error: Se esperaba {expected_url}, pero la URL final es {current_url}.")

except Exception as e:
    print(f"Error en la prueba: {e}")

finally:
    driver.quit()
