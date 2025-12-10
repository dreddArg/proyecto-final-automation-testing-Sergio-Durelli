from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory(login_in_driver):

    try:
        driver = login_in_driver

        # Compruebo el Título de la pestaña
        assert driver.title == "Swag Labs", "El título de la pastaña no es Swag Labs."
        print(f"Título de pestaña correcto = {driver.title}")

        # Obtenemos listado de productos presentados por la web
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # Comprobamos que el listado de productos sea superior a cero
        assert len(products) > 0, "Sin productos en página."
        print(f"Cantidad de productos listados: {len(products)}")

        # Tomamos primer producto e imprimo nombre y precio
        print(f"Informacion de Primer Producto:\nNombre: {products[0].find_element(By.CLASS_NAME,"inventory_item_name").text}\nPrecio: {products[0].find_element(By.CLASS_NAME,"inventory_item_price").text}")

        # Verificamos que el menu hamburguesa este visible
        assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), "No se encontró menu hamburguesa."
        print("Menú hamburguesa encontrado.")

        # Verificamos filtro para ordenar visible
        assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "No se encontró filtro para ordenar productos."
        print("Filtro de orden de productos encontrado.")
    
    except Exception as e:
        print(f"Error test_inventory: {e}")
        raise
