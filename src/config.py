import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

encoded_password = quote_plus(DB_PASSWORD) if DB_PASSWORD else ''
# Connection string for psycopg2
DATABASE_URL = f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"