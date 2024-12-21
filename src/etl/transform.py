from utils.logging_config import logging
import pandas as pd
from etl.extract import extractor
from pathlib import Path


logger = logging.getLogger(__name__)


def transformer(data, save_to_csv=False):
    """
    Transforms data in data.csv:

    converts "signup_date" column to a standard datetime format;
    filters "email" column, deletes not valid records;
    adds a new column "domain", containing domains of "email" column.

    Additionally, can save transformed data to the new .csv file "tranformed_data.csv".
    :param save_to_csv: Set "True" if you need to save transformed data as .csv file.
    :return: data — transformed pandas.DataFrame object from data.csv
    """
    try:
        logger.info('Starting to transform data...')

        data['signup_date'] = pd.to_datetime(data['signup_date']).dt.normalize()
        logger.debug('Normalized datetime format.')

        # Only takes 3 domains because "Faker().free_email_domain()" consist of them.
        invalid_email_indexes = data[(~data['email'].str.contains(r'.{5,}@(?:gmail|yahoo|hotmail)\.', regex=True))].index
        data.drop(invalid_email_indexes, inplace=True)
        logger.debug('Filtered out invalid emails.')

        data['domain'] = data['email'].str.split('@').str[-1]
        logger.debug('Added column "domain".')

        if save_to_csv:
            transformed_data_path = Path(__file__).parents[1] / 'data' / 'transformed_data.csv'
            data.to_csv(transformed_data_path, index=False)
            logger.info('Saved transformed data to "transformed_data.csv"')

        logger.info('Transforming completed.')
        return data
    except Exception as e:
        logger.error(f'Got an error: {e}\n')
