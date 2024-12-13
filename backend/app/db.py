# pip install pymongo
from app import app
from pymongo import MongoClient
import urllib.parse
import os


username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

db_client = MongoClient(
    f"mongodb+srv://{urllib.parse.quote(username)}:"f"{urllib.parse.quote(password)}@ci-cd-db.m4jsc.mongodb.net/?retryWrites=true&w=majority&appName=ci-cd-db")
app_db = db_client.app  # or db_client["app"]; here app is db name
user_collection = app_db.users  # or app_db["products]; here products is colln name


