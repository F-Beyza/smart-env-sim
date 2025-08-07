# src/data_handler/data_handler.py

from mongo_handler.mongo_handler import MongoHandler
import logging

class DataHandler:
    def __init__(self):
        self.mongo = MongoHandler()
        self.logger = logging.getLogger("DataHandler")

    def insert_data(self, data: dict):
        # Buraya validasyon veya filtreleme de eklenebilir
        try:
            self.mongo.insert_data(data)
            self.logger.info("Data successfully handled and stored.")
        except Exception as e:
            self.logger.error(f"DataHandler failed: {e}")
