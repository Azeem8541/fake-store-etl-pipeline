import logging

from etl.extract import extract_products, extract_users
from etl.load import get_engine, load_to_postgres
from etl.transform import transform_products, transform_users

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    logger.info("Pipeline started")

    products_raw = extract_products()
    users_raw = extract_users()

    products = transform_products(products_raw)
    users = transform_users(users_raw)
    logger.info("Transformation completed")

    engine = get_engine()
    load_to_postgres(products, "products", engine)
    load_to_postgres(users, "users", engine)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()