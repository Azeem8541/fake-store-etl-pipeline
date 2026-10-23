import logging
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()
logger = logging.getLogger(__name__)


def get_engine():
    url = URL.create(
        "postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 5432)),
        database=os.getenv("DB_NAME"),
    )
    return create_engine(url)


def load_to_postgres(df: pd.DataFrame, table_name: str, engine) -> None:
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    logger.info("Loaded %d rows into table '%s'", len(df), table_name)