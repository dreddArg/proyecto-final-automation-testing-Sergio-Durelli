import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    # Creamos opciones para el Chrome
    options = webdriver.ChromeOptions()

    # Sesion en modo incognito, impide pop-up de contraseña insegura
    options.add_argument("--incognito")

    # Definimos navegador con opciones cargadas
    driver = webdriver.Chrome(options=options)

    # Establecemos espera implicita gral
    driver.implicitly_wait(5)

    # Devolvemos el driver para utilizarlo
    yield driver

    # Luego de ejecutar tests, lo cerramos
    driver.quit()

@pytest.fixture
def login_in_driver(driver,usuario,password):
    LoginPage(driver).abrir_pagina().login_completo(usuario,password)
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_29469299270f461db0088a385a1eda7f"}