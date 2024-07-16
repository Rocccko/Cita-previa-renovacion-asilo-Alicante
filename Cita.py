
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')



datos = [{"passaporte": "TuPasaporte", "nombre": "TuNombre",
          "nacimiento": 1111, "Pais": "TuPais"}]


try:
    cookies = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cookie_action_close_header"))
    )
    cookies.click()
except:
    pass


# Elegir la opción 4 del menú desplegable de provincias, Alicante
def province():
    driver.find_element(By.XPATH, "//*[@id='form']/option[4]").click()

province()

driver.implicitly_wait(15)

def aceptbutton():
    driver.find_element(By.XPATH, "//*[@id='btnAceptar']").click()

aceptbutton()

# Elegir la opción 7 del menú de trámites policía nacional, que es expedición/renovación documentos asilo. 
def procedure():
    driver.find_element(
        By.XPATH, "//*[@id='tramiteGrupo[1]']/option[7]").click()  # ->solicitud de asilo

procedure()

driver.implicitly_wait(30)

aceptbutton()

def enter():
    driver.find_element(By.XPATH, "//*[@id='btnEntrar']").click()

enter()


# definir el número de veces que se enviarán los datos
repeat = 600

datos_enviados = set()
datos_enviados = []
for dato in datos:
    for i in range(repeat):

        pasport = driver.find_element(By.XPATH, "//*[@id='txtIdCitado']")
        nombre = driver.find_element(By.XPATH, "//*[@id='txtDesCitado']")
        year = driver.find_element(By.XPATH, "//*[@id='txtAnnoCitado']")
        pais = driver.find_element(By.XPATH, "//*[@id='txtPaisNac']")

        
        # ingresar los datos
        pasport.send_keys(dato["passaporte"])
        nombre.send_keys(dato["nombre"])
        year.send_keys(dato["nacimiento"])
        pais.send_keys(dato["Pais"])
        driver.find_element(By.XPATH, "//*[@id='btnEnviar']").click()

        # enviar el formulario
        driver.find_element(By.XPATH, "//*[@id='btnSubmit']").click()
        
        # se repite x veces
        province()
        
        driver.implicitly_wait(15)
        
        aceptbutton()

        driver.find_element(
            By.XPATH, "//*[@id='tramiteGrupo[1]']/option[7]").click()

        driver.implicitly_wait(30)

        aceptbutton()
        enter()
if repeat == 600:
    driver.quit()
