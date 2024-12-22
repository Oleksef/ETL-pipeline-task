import faker
import pandas as pd
from utils.logging_config import logging
from utils.data_config import data_path, csv_path
from pathlib import Path
import random


logger = logging.getLogger(__name__)


def generator():
    """
    Generates synthetic data in English
    :return:
    """
    logger.debug('Starting to generate data...')

    try:
        fake = faker.Faker()
        data = pd.DataFrame()
        for i in range(1, 10000):
            data.loc[i, 'user_id'] = i
            data.loc[i, 'name'] = fake.name()
            data.loc[i, 'email'] = random.choice((fake.free_email(), fake.email(), fake.domain_name()))
            data.loc[i, 'signup_date'] = fake.date_time_this_year()

        data['user_id'] = data['user_id'].astype(int)
        data.to_csv(csv_path, index=False)
    except Exception as e:
        logger.error(f'Got an error: {e}\n')


def extractor():
    """
    Extracts data from .csv file
    :return: data — pandas.DataFrame object from data.csv
    """
    logger.info('Starting to extract data...')

    if not Path(csv_path).exists():
        generator()

    try:
        data = pd.read_csv(csv_path)
        logger.info('Extracting completed.')
        return data
    except Exception as e:
        logger.error(f'Got an error: {e}\n')
