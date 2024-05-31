import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt="%y-%d-%m %H:%M:%S %p")

# Create file handler
fh = logging.FileHandler("Automation.logs")
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

# Add file handler to the logger
logger.addHandler(fh)

def configure_logger():
    return logger