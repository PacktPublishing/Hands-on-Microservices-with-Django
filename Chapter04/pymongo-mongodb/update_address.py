from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

con = "mongodb+srv://django-microservice:<password>@<cluster>/?retryWrites=true&w=majority"
client = MongoClient(con, server_api=ServerApi('1'))
db = client["Subscription"]
col = db["subscription_address"]

col.update_one(
    {"name": "Monthy Python"},
    {"$set": {"address": "Liverpool Street"}}
)
