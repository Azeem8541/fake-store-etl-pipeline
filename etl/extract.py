import logging

import pandas as pd
import requests

BASE_URL = "https://fakestoreapi.com"
logger = logging.getLogger(__name__)


def _fetch(endpoint: str) -> pd.DataFrame:
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    logger.info("Extracted %d rows from /%s", len(df), endpoint)
    return df


def extract_products() -> pd.DataFrame:
    return _fetch("products")


def extract_users() -> pd.DataFrame:
    return _fetch("users")