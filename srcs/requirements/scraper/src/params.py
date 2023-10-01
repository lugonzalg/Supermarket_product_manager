from Logger import logger
import yaml
import sys
import os

PARAMS = os.environ["PARAMS"]

try:
    with open(PARAMS, 'r') as config_file:
        config_data = yaml.safe_load(config_file)
except FileNotFoundError as file_error:
    logger.logger.error(f"Error: {file_error}")
    sys.exit(1)

postgres = config_data["postgres"]
PG_CREDENTIALS = postgres["credentials"]
PG_HOSTNAME = postgres["hostname"]
PG_DATABASE = postgres["database"]
PG_USER = PG_CREDENTIALS["username"]
PG_PASSWORD = PG_CREDENTIALS["password"]

scraper = config_data["scraper"]
PROJECT_NAME = scraper["project_name"]
urls = scraper["urls"]
URL_CATEGORIES = urls["categories"]

BASIC_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
