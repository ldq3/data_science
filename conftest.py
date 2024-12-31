import logging
import os

def pytest_configure(config):
    log_file = os.path.join(os.getcwd(), "log/test.log")
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='w'
    )
