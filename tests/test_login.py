from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from utils.datos import leer_csv_login

@pytest.mark.parametrize("usuario,password,debe_loguear",leer_csv_login("datos/data_login.csv"))
def test_login_valid(login_in_driver,usuario,password,debe_loguear):

    try:
        # Usamos funcion login
        driver = login_in_driver   

        # prueba de usuario bien
        if debe_loguear:
            # Prueba de redireccionamiento a web inventario
            assert "/inventory.html" in driver.current_url, "No se realizo el login y la redireccion a la web inventory.html"
            print("Login y redireccionamiento exitoso.")
        
        #prueba de usuario incorrecto
        elif debe_loguear == False:
            mensaje_error = LoginPage(driver).obtener_error()
            assert "Epic sadface" in mensaje_error, "El mensaje de error en logueo no se esta mostrando correctamente"

    except Exception as e:
        print(f"Error test_login: {e}")
        raise
