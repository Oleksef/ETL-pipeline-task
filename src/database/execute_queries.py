from sqlalchemy import text
from pathlib import Path

from sqlalchemy.orm import sessionmaker

from utils.logging_config import logging
logger = logging.getLogger(__name__)


def executor(engine):
    """
    Executes SQL queries from a "sql" folder.
    :param engine: SQLAlchemy engine.
    """
    try:
        logger.info(f"Executing SQL files.")

        sql_folder = Path(__file__).parents[2] / 'sql'
        sql_files = [f for f in Path(sql_folder).glob('*.sql') if f.suffix == '.sql']
        print(sql_folder)
        print(sql_files)

        if not sql_files:
            logger.warning("SQL files weren't finded.")
            return

        Session = sessionmaker(bind=engine)
        session = Session()

        for file in sql_files:
            file_path = Path(sql_folder) / file
            logger.info(f"Executing SQL file: {file}")
            with open(file_path, 'r') as f:
                sql_query = f.read()
                session.execute(text(sql_query))
                logger.info(f"Successfully executed.")

        session.commit()
    except Exception as e:
        logger.error(f"Got an error: {e}\n")
    finally:
        session.close()
