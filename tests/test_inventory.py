from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# importamos el logger
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):

    try:
        logger.info(f"Iniciando login con los datos de usuario: {usuario} y password: {password}")
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"Intento de login completado")

        # Instanciar pagina con funciones desde la clase
        inventory_page = InventoryPage(driver)

        # Comprobamos que el listado de productos sea superior a cero
        logger.info(f"Prueba de productos listados mayor a cero")
        assert len(inventory_page.get_products()) > 0, "Sin productos en página."
        logger.info(f"Productos listados: {len(inventory_page.get_products())}")
        print(f"Cantidad de productos listados: {len(inventory_page.get_products())}")

        # comprobamos carrito vacio al inicio
        logger.info(f"Prueba de carrito vacio al ingresar")
        assert inventory_page.get_cart_count() == 0
        logger.info(f"Items en el carrito: {inventory_page.get_cart_count()}")

        # agregamos el primer producto al carrito
        logger.info(f"Prueba agregar primer producto al carrito")
        inventory_page.add_first_product()
        # comprobar contador del carrito
        assert inventory_page.get_cart_count() == 1
        logger.info(f"Items en el carrito: {inventory_page.get_cart_count()}")
    
    except Exception as e:
        print(f"Error test_inventory: {e}")
        raise
