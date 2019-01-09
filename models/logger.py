""" Configure logger """
import logging
import os.path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
                              datefmt='%d/%m/%Y %H:%M:%S')
if not os.path.exists("logs/"):
    os.makedirs("logs/")
file_handler = logging.FileHandler(f'logs/store.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
