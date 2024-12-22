from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

data_path = os.getenv('CSV_PATH', Path(__file__).parents[1] / 'data')
csv_path = str(data_path) + '\\data.csv'
transformed_csv_path = str(data_path) + '\\transformed_data.csv'