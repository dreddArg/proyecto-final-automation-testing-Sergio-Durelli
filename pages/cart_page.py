from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:

    # Selectores de web carrito
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def get_cart_products(self):
        # esperamos y retornamos el item en el carrito
        return self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
    
    def get_cart_product_name(self):
        # esperamos y retornamos el nombre del producto en el carrito
        return self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME)).text