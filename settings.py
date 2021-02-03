from os import getenv
from dotenv import load_dotenv

load_dotenv()

search_url = getenv('SEARCH_URL')
db_url = getenv('DB_URL')