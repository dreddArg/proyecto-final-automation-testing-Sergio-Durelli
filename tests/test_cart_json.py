from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.lector_json import read_json_products

import time

RUTA_JSON = "datos/productos.json" #constante con ruta del archivo

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("name_product",read_json_products(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,name_product):
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        inventory_page.add_product_by_name(name_product)

        # Abrir el carrito
        inventory_page.open_cart()

        # espera para q cargue la web
        time.sleep(1)

        # Validar el nombre de producto, usamos cart page para obtener datos
        cart_page = CartPage(driver)

        assert cart_page.get_cart_product_name() == name_product
        

    except Exception as e:
        print(f"Error en test_cart_json: {e}")
        raise