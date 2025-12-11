from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    
    # selectores de pagina web
    _INVENTORY_ITEMS = (By.CLASS_NAME,"inventory_item")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item button")
    _CART_COUNT = (By.CLASS_NAME,"shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")
    _CART_LINK = (By.CLASS_NAME,"shopping_cart_link")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def get_products(self):
        # espero listado completo de items
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        # retorno elementos desenpaquetados
        return self.driver.find_elements(*self._INVENTORY_ITEMS)
    
    def get_products_names(self):
        # armo listado desenpaquetado de items
        products = self.driver.find_elements(*self._ITEM_NAME)
        # extraigo nombres de productos
        return [product_name.text for product_name in products]
    
    def add_first_product(self):
        # espero y recojo listado de items
        products = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS)) 
        # desenpaqueto items y busco el boton del producto en ubicacion 0
        first_product_button = products[0].find_element(*self._ADD_TO_CART_BUTTON)
        # hago click en el boton del primer producto
        first_product_button.click()

    def add_product_by_name(self,product_name):
        # armo lista de productos
        products = self.driver.find_elements(*self._INVENTORY_ITEMS)   

        # recorremos listado de productos
        for product in products:
            # sacamos el nombre de cada producto
            name = product.find_element(*self._ITEM_NAME).text
            # comparamos el nombre buscado
            if name.strip() == product_name.strip():
                # si lo encuentra hacemos click en su botón
                button = product.find_element(*self._ADD_TO_CART_BUTTON)
                button.click()
                return self
        # en caso de no encontrarlo en la lista, devolvemos una excepción
        raise Exception(f"No se encontro el producto {product_name}")
    
    def open_cart(self):
        # esperamos a q este la posibilidad de hacer click en el link al carrito y hacemos click
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()
        return self
    
    def get_cart_count(self):
        try:
            # esperamos la visibilidad del contador del carrito
            self.wait.until(EC.visibility_of_element_located(self._CART_COUNT))
            # separamos el valor numerico del contador y lo retornamos como un int 
            cart_count = self.driver.find_element(*self._CART_COUNT)
            return int(cart_count.text)
        except:
            # en caso de no encontrar el contador del carrito devolvemos un valor de cero
            return 0