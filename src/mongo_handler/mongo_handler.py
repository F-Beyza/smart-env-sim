# src/mongo_handler/mongo_handler.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoHandler:
    def __init__(self, db_name="smart_env_db", collection_name="sensor_data"):
        uri = os.getenv("MONGODB_URI")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data: dict):
        result = self.collection.insert_one(data)
        print(f"[✓] Data inserted with ID: {result.inserted_id}")
