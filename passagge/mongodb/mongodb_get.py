from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import json
import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


load_dotenv()

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


count = collection.count_documents({})
logger.info(f"Count of documents in collection: {count}")


'''
# Find first record in collection:
filter = {'title': 'юбка'}
documents = collection.find_one(filter)
logger.info(documents)

# RESULT:
# 2023-05-18 00:27:09:27S - root - INFO - {
# '_id': ObjectId('6465404fe4a9c7ea27f62220'), 'title': 'юбка', 'sku': 'FN-WN-SKIR000099', 
# 'color': 'DUSTYORANGE/персиковый', 'brand': 'Acne Studios', 'sex': 'Ж', 'material': ' 100% полиэстер', 
# 'size_table_type': 'Одежда Ж Германия', 'root_category': 'Одежда без маркировки', 
# 'fashion_season': '2019-2', 'fashion_collection': 'Acne Studios Donna FW 2019', 
# 'fashion_collection_inner': 'Acne Studios Womens RTW Main', 'manufacture_country': 'КИТАЙ', 
# 'category': 'юбка', 'price': 11990, 'discount_price': 8990, 'in_the_sale': True, 
# 'leftovers': [{'size': '36', 'count': 1, 'price': 8990}, {'size': '38', 'count': 1, 'price': 8990}]}
'''

filter = {"title": "юбка", "price": 37500}

documents = collection.find_one(filter)
logger.info(documents)
# for document in documents:
#     logger.info(document)

# 2023-05-18 00:47:01:47S - root - INFO - {'_id': ObjectId('6465404fe4a9c7ea27f62225'), 'title': 'юбка', 'sku': 'A-04-4001-000-1', 'color': 'BLACK/черный', 'brand': 'Anine Bing', 'sex': 'Ж', 'material': ' 100% шёлк', 'size_table_type': 'Буквы Ж', 'root_category': 'Одежда без маркировки', 'fashion_season': '2022-1', 'fashion_collection': 'Anine Bing Donna SS 2022', 'fashion_collection_inner': 'Anine Bing Womens RTW Precollection', 'manufacture_country': 'КИТАЙ', 'category': 'юбка', 'price': 37500, 'discount_price': 23630, 'in_the_sale': True, 'leftovers': [{'size': 'L', 'count': 0, 'price': 23630}, {'size': 'M', 'count': 0, 'price': 23630}, {'size': 'S', 'count': 0, 'price': 23630}]}
# 2023-05-18 00:47:01:47S - root - INFO - {'_id': ObjectId('6465404fe4a9c7ea27f622cc'), 'title': 'юбка', 'sku': '4021371', 'color': 'LIGHTBEIGE/бежевый', 'brand': 'Maurizio', 'sex': 'Ж', 'material': ' 72% лен,10% хлопок,6% полиамид,6% полиэстер,6% вискоза', 'size_table_type': 'Буквы Ж', 'root_category': 'Одежда без маркировки', 'fashion_season': '2021-1', 'fashion_collection': 'Maurizio Donna SS 2021', 'fashion_collection_inner': 'Maurizio Womens RTW fashion', 'manufacture_country': 'ИТАЛИЯ', 'category': 'юбка', 'price': 37500, 'discount_price': 13130, 'in_the_sale': True, 'leftovers': [{'size': 'L', 'count': 1, 'price': 13130}, {'size': 'S', 'count': 1, 'price': 13130}]}
