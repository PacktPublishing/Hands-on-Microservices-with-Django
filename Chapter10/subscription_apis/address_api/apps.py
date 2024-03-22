import os
import redis

from django.apps import AppConfig
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class AddressApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'address_api'

    def ready(self) -> None:
        if os.environ.get('RUN_MAIN'):
            redis_client = redis.Redis(host='redis', port=6379)

            con = "mongodb+srv://django-microservice:<password>@<cluster>/?retryWrites=true&w=majority"
            client = MongoClient(con, server_api=ServerApi('1'))
            db = client["Subscription"]
            address_col = db["address_api_address"]

            redis_client.delete('addresses')

            for address in address_col.find():
                redis_client.lpush('addresses', address["address"])

            print('Addresses added to Redis cache')
