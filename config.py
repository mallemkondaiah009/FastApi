
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:smk4305a@mongolearn.rxwn2zn.mongodb.net/?retryWrites=true&w=majority&appName=mongolearn"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), connectTimeoutMS=30000)  # 30 seconds

db = client.todo_db
collection = db["todo_data"]