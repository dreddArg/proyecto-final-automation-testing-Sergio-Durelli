from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from utils.datos import leer_csv_login

from utils.logger import logger

@pytest.mark.parametrize("usuario,password,debe_loguear",leer_csv_login("datos/data_login.csv"))
def test_login_valid(login_in_driver,usuario,password,debe_loguear):

    try:
        # Usamos funcion login
        logger.info(f"Completando login con los datos de usuario: {usuario} y password: {password}")
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

        # prueba de usuario bien
        if debe_loguear:
            # Prueba de redireccionamiento a web inventario
            logger.info("Prueba de redireccionamiento a web inventario")
            assert "/inventory.html" in driver.current_url, "No se realizo el login y la redireccion a la web inventory.html"
            logger.info("test de login completado")
            print("Login y redireccionamiento exitoso.")
        
        #prueba de usuario incorrecto
        elif debe_loguear == False:
            logger.info("Prueba de login erroneo")
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "El mensaje de error en logueo no se esta mostrando correctamente"
            logger.info("Prueba de login erroneo completado")

    except Exception as e:
        print(f"Error test_login: {e}")
        raise
