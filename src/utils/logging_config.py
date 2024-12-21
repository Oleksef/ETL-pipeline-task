from dotenv import load_dotenv
import os
from pathlib import Path
import logging
from datetime import datetime

load_dotenv()

log_level = os.getenv('LOG_LEVEL', 'INFO')
log_format = os.getenv('LOG_FORMAT', '%(asctime)s %(levelname)s | %(name)s | %(message)s')
log_path = os.getenv('LOG_PATH', Path(__file__).parents[2] / 'logs')
log_filename = str(log_path) + f'\\{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

logging.basicConfig(level=log_level, format=log_format, filename=log_filename)
