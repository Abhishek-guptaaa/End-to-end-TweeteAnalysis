from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pandas as pd


def read_mongo_data():
    """Read data from MongoDB collection and convert to DataFrame."""
    client=None
    try:
        pass
    except Exception as e:
        