# Entrega Automation Testing - Sergio Durelli

## Propósito del Proyecto

El objetivo del proyecto es aplicar los conocimientos obtenidos hasta la clase 8 del curso, se automatizó el flujo básico de navegación web en base a Python, Selenium WebDriver en Chrome. El sitio objetivo de las pruebas es https://www.saucedemo.com/, una aplicación web demo diseñada para prácticas de testing.

## Tecnologías Utilizadas
- **Lenguaje**: Python
- **Framework**: Selenium WebDriver
- **Pruebas**: pytest
- **Brower**: Chrome Browser
- **Plugin Reports**: pytest-html

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
3. Instalar la libreria Webdriver Manager for Python:
   ```
   pip install webdriver-manager
   ```

## Ejecución de las Pruebas
Para ejecutar las pruebas del proyecto, utilice el siguiente comando manualmente en su consola:
```
py run_tests.py
```
Esto generará un informe en formato HTML llamado `report_tests.html` en la carpeta `reports` con los resultados de las pruebas.