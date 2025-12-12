import logging
import pathlib

# definimos el path para archivar los logs
log_dir = pathlib.Path('logs')
# si no existe, creamos la carpeta
log_dir.mkdir(exist_ok=True)

# nombre completo del archivo con su ruta
log_file = log_dir/ 'automationQA.log'

# instanciamos el logger
logger = logging.getLogger("AutoQA")
# tipo de logs a capturar
logger.setLevel(logging.INFO)

# prueba de si existen datos en el handlers
if not logger.handlers:
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8") # mode "a" de append

    # formateo de los logs
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # aplicar formato y setear
    file_handler.setFormatter(formatter)
    # agregar al logger
    logger.addHandler(file_handler)