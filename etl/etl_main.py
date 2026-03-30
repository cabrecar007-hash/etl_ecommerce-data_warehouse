import yaml
from extract import load_store_logs
from transform import transform_logs
from load import load_to_dw
import logging

# Setup logging
logging.basicConfig(filename='logs/etl.log', level=logging.INFO)

# Load configs
with open('config/db_config.yaml') as f:
    db_config = yaml.safe_load(f)

with open('config/stores_config.yaml') as f:
    stores_config = yaml.safe_load(f)

for store in stores_config['stores']:
    logging.info(f"Starting ETL for store: {store['name']}")
    rows = load_store_logs(store, db_config['mysql'])
    transformed = transform_logs(rows, store['store_id'])
    load_to_dw(transformed, db_config['postgresql'])
    logging.info(f"Finished ETL for store: {store['name']}")
