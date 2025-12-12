from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest 

from pages.login_page import LoginPage

# importamos faker
from faker import Faker

# inicializamos el faker
fake = Faker()

@pytest.mark.parametrize("usuario,password,debe_loguear", [
    (fake.user_name(),fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True),False),
    (fake.user_name(),fake.password(),False),
])
def test_login_valid(login_in_driver,usuario,password,debe_loguear):

    try:
        # Usamos funcion login
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)

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
        print(f"Error test_login_faker: {e}")
        raise
