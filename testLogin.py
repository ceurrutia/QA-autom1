from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar Chrome SIN HEADLESS para ver si funciona
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")


# Instalar y configurar ChromeDriver automáticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    print("Abriendo página de login")
    driver.get("https://auth.educacionit.com/authorize?redirect_uri=https%3A%2F%2Falumni.education%2Fauth-return&state=eyJxdWVyeSI6e319&client_id=D953231B-E6AB-4734-9B7F-A24999B8DE5B")

    
    print("Buscando los campos de usuario y contraseña...")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "form-email"))  
    )
    password_field = driver.find_element(By.ID, "form-password") 

    # Ingresar  credenciales proporcionadas
    print("Ingresando credenciales...")
    username_field.send_keys("credenciales_proorcionadas@g.com")  
    password_field.send_keys("Tu_pass")  

    
    print("Buscando el botón de Acceder")
    #Selector complejo
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__nuxt > main > div > div.flex.flex-col.gap-6.items-center.bg-white.w-full.h-full.my-auto.mx-auto.xs\\:h-auto.xs\\:w-\\[448px\\].px-5.py-6.xs\\:p-16.rounded-lg > form > button"))
    )

    print("Haciendo clic en 'Acceder'")
    login_button.click()

    
    print("Esperando la redirección")
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

    # URL actual después del login
    current_url = driver.current_url
    print(f"URL actual luego del login es: {current_url}")

    # URL esperada 
    expected_url = "https://alumni.education/courses" 
    if current_url == expected_url:
        print("Login exitoso")
    else:
        print(f"Error, la url no es la esperada")

except Exception as e:
    print(f"La prueba ha fallado: {e}")

finally:
    time.sleep(5)
    print("Cerrando navegador")
    driver.quit()
