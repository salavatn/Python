from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import logging.config
import logging
import os


logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger()

load_dotenv(dotenv_path='config/.env')

mongodb_pswd = os.getenv('MONGODB_PSWD')
uri = f"mongodb+srv://salavat:{mongodb_pswd}@nsa.efbawfy.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    logger.info("Connected successfully to MongoDB!")
except Exception as error:
    logger.error("Could not connect to MongoDB")

db = client['internet_market']
collection = db['ppassage_market']
