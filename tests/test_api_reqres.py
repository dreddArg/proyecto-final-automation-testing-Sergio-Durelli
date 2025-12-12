import requests
import pytest
from utils.logger import logger

# request de usuario ID 2
def test_get_user(url_base,header_request):
    logger.info(f"API: Solitud GET de usuario ID 2 a: {url_base}/2")
    response = requests.get(f"{url_base}/2",headers=header_request)

    logger.info(f"API: Status code: {response.status_code} = 200")
    assert response.status_code == 200
    logger.info("API: Response 200 OK")
    data = response.json()

    logger.info("API: Validando el id 2 dentro de la respuesta")
    assert data["data"]["id"] == 2
    logger.info("API: Id 2 validado")
    
# request para crear usuario
def test_create_user(url_base,header_request):
    payload={
        "name": "Jose",
        "job": "Profesor"
    }
    logger.info(f"API: Solitud POST para crear usuario")
    response = requests.post(url_base,headers=header_request,json=payload)
    
    logger.info(f"API: Status code: {response.status_code} = 201")
    assert response.status_code == 201
    
    logger.info(f"API: Prueba de name en payload vs recibido de la API")
    data = response.json()

    assert data["name"] == payload["name"]

# request de Eliminar usuario
def test_delete_user(url_base,header_request):
    logger.info(f"API: Solitud POST para eliminar usuario 2")
    response = requests.delete(f"{url_base}/2",headers=header_request)

    logger.info(f"API: Prueba de status code: {response.status_code} = 204")
    assert response.status_code == 204
