import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime
#import time

target = pathlib.Path("reports/screenshots")
target.mkdir(parents=True, exist_ok=True) # parents=True crea carpetas necesarias hasta la carpeta final

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
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_29469299270f461db0088a385a1eda7f"}

@pytest.hookimpl(hookwrapper=True) # hookwrapper, ejecuta el test e incorpora el codigo de captura de pantalla dentro del test
def pytest_runtest_makereport(item,call): # item es el test y fixtures que ejecuta, call informacion
    outcome = yield # return sin cerrar la funcion, pausa la ejecucion, permite reanudar luego

    report = outcome.get_result()

    # condicion para disparar captura, setup=config previa a ejecucion, call=ejecucion del test
    if report.when in ("setup","call") and report.failed:
        # de la variable del test en ejecucion, trae argumentos/fixtures, si no encuentra asigna None
        driver = item.funcargs.get("driver",None)
        
        # si tenemos datos en el momento que falló, capturamos el momento
        if driver:
            timestamp_comun= datetime.now().strftime("%Y%m%d_%H%M%S")
            #timestamp_unix = int(time.time())
            file_name= target / f"{report.when}_{item.name}_{timestamp_comun}.png" # nombre de la imagen
            # guardamos la screenshot 
            driver.save_screenshot(str(file_name))