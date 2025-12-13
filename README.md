# Entrega Automation Testing Talento Tech - Sergio Durelli

## Propósito del Proyecto

El objetivo del proyecto es aplicar los conocimientos obtenidos en todo el curso, se incorporaron prácticas de Page Object Model, manejo de datos externos (JSON, CSV), generacion de reportes HTML, logging y screenshots de errores y pruebas de una API Rest. El sitio objetivo de las pruebas es https://www.saucedemo.com/, una aplicación web demo diseñada para prácticas de testing. Y la API utilizada para las pruebas fue: https://reqres.in/

## Tecnologías Utilizadas
- **Lenguaje**: Python 3.x
- **Framework**: Selenium WebDriver
- **Pruebas**: pytest
- **Brower**: Chrome Browser
- **Plugin Reports**: pytest-html
- **Librerias Adicionales**: Logging, Faker, Request, csv, pathlib, json

## Instrucciones de Instalación de Dependencias
Para instalar las dependencias del proyecto, sigue estos pasos:

1. Instalar la libreria pytest y plugin reportes:
   ```
   pip install pytest pytest-html
   ```
2. Instalar la libreria Selenium:
   ```
   pip install selenium
   ```
3. Instalar la libreria Webdriver Manager para Python:
   ```
   pip install webdriver-manager
   ```
4. Instalar la libreria Faker para Python:
   ```
   pip install faker
   ```
5. Instalar la libreria Requests para pruebas de APIs con Python:
   ```
   pip install requests
   ```

## Reportes y Logs

El proyecto captura tres fuentes principales de información durante la ejecución de las pruebas: **reporte HTML** general, **capturas de pantalla** en caso de error y un **archivo de log** completo.

### Reporte HTML
Se genera un reporte HTML detallado en la carpeta **reports** con el nombre de ```report.hmtl```
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas
### Logs de ejecución
Tambien se genera un log con informacion detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/automationQA.log```

### Capturas de pantalla

Se realizan capturas de pantalla por cada test que haya fallado y se encuentran en la siguiente ubicacion: ```reports/screenshots/```

## Ejecución de las Pruebas
Para ejecutar las pruebas del proyecto, utilice el siguiente comando manualmente en su consola:
```bash
python -m run_tests.py
```
O
```bash
py run_tests.py
```
## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la pagina de inventario, agregar primer producto
- Comportamiento de la pagina del carrito, agregar producto por nombre
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP (status code), validaciones de estructura JSON en respuesta.

## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios validos o invalidos
    - `productos.json` -> datos de productos para validacion

## Conclusión
El proyecto plantea una estructura organizada y escalable para automatizar pruebas de API y webs utilizando Python/Pytest generando reportes HTML y logs facilitando el análisis de los resultados.

Se aplicaron buenas practicas de programación con una arquitectura preparada para una escalabilidad aceptable a largo plazo.