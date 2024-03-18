# celery -A celery_worker worker -l info
import datetime
from celery import Celery
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from time import sleep

app = Celery('log', broker='pyamqp://guest@localhost//')


@app.task()
def write_logitem(application, logmessage):
    sleep(5)
    now = datetime.datetime.now()

    uri = "mongodb+srv://django-microservice:<password>@<cluster>/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    subscription_db = client["Subscription"]
    logitem_col = subscription_db["subscription_logitem"]

    logitem_col.insert_one({'time': now.strftime('%Y-%m-%d %H:%M:%S'),
                            'app': application,
                            'logmessage': logmessage})

    return "Log message entered"
