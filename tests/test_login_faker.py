from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest 

from pages.login_page import LoginPage

# importamos faker
from faker import Faker

# inicializamos el faker
fake = Faker()

# importamos el logger
from utils.logger import logger

@pytest.mark.parametrize("usuario,password,debe_loguear", [
    (fake.user_name(),fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True),False),
    (fake.user_name(),fake.password(),False),
    (fake.user_name(),fake.password(),False),
])
def test_login_faker(login_in_driver,usuario,password,debe_loguear):

    try:
        # Usamos funcion login
        logger.info(f"Iniciando login con los datos de usuario: {usuario} y password: {password}")
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"Intento de login completado")

        # prueba de usuario bien
        if debe_loguear:
            # Prueba de redireccionamiento a web inventario
            logger.info("Prueba de redireccionamiento a web inventario")
            assert "/inventory.html" in driver.current_url, "No se realizo el login y la redireccion a la web inventory.html"
            logger.info("Login y redireccionamiento correcto.")
            print("Login y redireccionamiento exitoso.")
        
        #prueba de usuario incorrecto
        elif debe_loguear == False:
            logger.info("Verificación de login incorrecto")
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "El mensaje de error en logueo no se esta mostrando correctamente"
            logger.info("Prueba de login incorrecto completado")

    except Exception as e:
        print(f"Error test_login_faker: {e}")
        raise
