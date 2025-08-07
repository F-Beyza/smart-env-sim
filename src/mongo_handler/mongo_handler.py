# src/mongo/mongo_handler.py

from pymongo import MongoClient
import logging

class MongoHandler:
    def __init__(self, db_name='smart_env_db', collection_name='sensor_data'):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.logger = logging.getLogger("MongoHandler")

   # def insert_data(self, data: dict):
    #    try:
     #       self.collection.insert_one(data)
      #      self.logger.info("[✓] Data inserted to MongoDB.")
       # except Exception as e:
        #    self.logger.error(f"[✗] Mongo insert failed: {e}")

    def insert_data(self, data: dict):
        print("[•] insert_data called with:", data)  # DEBUG
        try:
            self.collection.insert_one(data)
            print("[✓] MongoDB insert successful.")
        except Exception as e:
            print(f"[✗] MongoDB insert failed: {e}")








# src/mongo_handler/mongo_handler.py FOR MONGODB ATLAS (cloud)

 #       import os
  #      from pymongo import MongoClient
   #     from dotenv import load_dotenv
#
 #       load_dotenv()
#
  #      class MongoHandler:
   #         def __init__(self, db_name="smart_env_db", collection_name="sensor_data"):
    #            uri = os.getenv("MONGODB_URI")
     #           self.client = MongoClient(uri)
      #          self.db = self.client[db_name]
       #         self.collection = self.db[collection_name]
#
 #           def insert_data(self, data: dict):
  #              result = self.collection.insert_one(data)
   #             print(f"[✓] Data inserted with ID: {result.inserted_id}")
