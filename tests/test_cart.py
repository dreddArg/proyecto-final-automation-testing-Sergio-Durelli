from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):

    try:
        logger.info(f"Iniciando login con los datos de usuario: {usuario} y password: {password}")
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        logger.info(f"Intento de login completado")
        inventory_page = InventoryPage(driver)

        # Obtenemos primer producto presentado por la web
        logger.info(f"Prueba de agregar a carrito primer producto")
        inventory_page.add_first_product()
        logger.info(f"Agregado completado")

        # abrimos carrito
        logger.info(f"Apertura de carrito")
        inventory_page.open_cart()

        # validar el producto si esta agregado al carrito
        cart_page = CartPage(driver)
        products_in_cart = cart_page.get_cart_products()
        logger.info(f"Prueba de 1 producto en carrito")
        assert len(products_in_cart) == 1, "El badge del carrito no aumento a 1."
        logger.info(f"Verificacion completada, productos en carrito: {len(products_in_cart)}")
        print("Cart badge aumentó a 1.")
        
    except Exception as e:
        print(f"Error test_cart: {e}")
        raise
