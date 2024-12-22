from sqlalchemy import create_engine, text
import os

from dotenv import load_dotenv
load_dotenv()

from utils.logging_config import logging
logger = logging.getLogger(__name__)

try:
    logger.debug('Connecting to database...')
    engine = create_engine(r'postgresql+psycopg2://{}:{}@{}:5432/{}'.format(
        os.getenv('POSTGRES_USER', 'postgres'), os.getenv('POSTGRES_PASSWORD', '<PASSWORD>'),
        os.getenv('POSTGRES_HOST', 'localhost'), os.getenv('POSTGRES_DB', 'postgres'))
        )
    logger.debug('Connection established.')
except Exception as e:
    logger.error(f'Got an error: {e}\n')


def create_table():
    try:
        with engine.connect() as conn:
            logger.debug('Creating table "users"...')
            conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        signup_date DATE NOT NULL,
                        domain VARCHAR(100) NOT NULL)
            """))
            logger.debug('Table "users" created.')
    except Exception as e:
        logger.error(f'Got an error: {e}\n')
