from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://django-microservice:<password>@<cluster>/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Subscription"]
col = db["subscription_address"]

col.delete_one({"name": "Monthy Python"})
