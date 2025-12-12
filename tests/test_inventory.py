from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):

    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        # Instanciar pagina con funciones desde la clase
        inventory_page = InventoryPage(driver)

        # Comprobamos que el listado de productos sea superior a cero
        assert len(inventory_page.get_products()) > 0, "Sin productos en página."
        print(f"Cantidad de productos listados: {len(inventory_page.get_products())}")

        # comprobamos carrito vacio al inicio
        assert inventory_page.get_cart_count() == 0

        # agregamos el primer producto al carrito
        inventory_page.add_first_product()
        # comprobar contador del carrito
        assert inventory_page.get_cart_count() == 1
    
    except Exception as e:
        print(f"Error test_inventory: {e}")
        raise
