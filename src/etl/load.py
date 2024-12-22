from database import db
import pandas as pd

from utils.logging_config import logging
logger = logging.getLogger(__name__)


def loader(data: pd.DataFrame):
    db.create_table()

    try:
        logger.info('Loading data to database...')
        data.to_sql('users', db.engine, if_exists='replace', index=False)
        logger.info('Loading completed.')
    except Exception as e:
        logger.error(f'Got an error: {e}\n')


