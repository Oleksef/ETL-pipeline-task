from etl import extractor, transformer, loader
from database.execute_queries import executor
from database.db import engine

if __name__ == "__main__":
    # ETL data process
    dataframe = extractor()
    transformed_dataframe = transformer(dataframe)
    loader(transformed_dataframe)

    # Execution of SQL queries
    executor(engine)