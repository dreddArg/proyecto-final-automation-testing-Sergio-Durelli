from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):

    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        inventory_page = InventoryPage(driver)

        # Obtenemos primer producto presentado por la web
        inventory_page.add_first_product()

        # abrimos carrito
        inventory_page.open_cart()

        # validar el producto si esta agregado al carrito
        cart_page = CartPage(driver)
        products_in_cart = cart_page.get_cart_products()
        assert len(products_in_cart) == 1, "El badge del carrito no aumento a 1."
        print("Cart badge aumentó a 1.")
        
    except Exception as e:
        print(f"Error test_cart: {e}")
        raise
