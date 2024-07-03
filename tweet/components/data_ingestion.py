import os
import sys
from tweet.logger import logging
from tweet.exception import CustomException
import pandas as pd
from mongo import read_mongo_data
from dataclasses import dataclass

@dataclass

class DataIngestionConfig():
    raw_data_path : str =os.path.join("artifacts", "raw.csv")


class DataIngestion():
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):

        try:
            # Check raw data file already exists
            if os.path.exists(self.ingestion_config.raw_data_path):
                logging.info("Raw data file already exists. Skipping ingestion.")
                return self.ingestion_config.raw_data_path
            
            # Read data from MongDB
            df=read_mongo_data()
            if df is None:
                logging.error("No data found to ingest")
                return None
            
            logging.info("Reading completed from MongoDB")

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data to CSV
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed")
            return self.ingestion_config.raw_data_path
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    di = DataIngestion()
    di.initiate_data_ingestion() 
