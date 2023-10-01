#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER $SCRAPER_USER WITH PASSWORD '$SCRAPER_PASS';
	CREATE DATABASE $SCRAPER_DB;
	GRANT ALL PRIVILEGES ON SCHEMA public TO $SCRAPER_USER;
	GRANT ALL PRIVILEGES ON DATABASE $SCRAPER_DB TO $SCRAPER_USER;
EOSQL

#/tmp/create_tables.sh
