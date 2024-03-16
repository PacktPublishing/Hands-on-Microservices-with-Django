import unittest
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from time import sleep
from .tasks import match_address_task, send_email_task


class MatchTest(unittest.TestCase):
    # Class variables for happy path tests matching mechanism
    base_id = 0
    base_street = ''
    variant_id = 0
    variant_street = ''

    # Class variable for boundary test
    last_id = 0

    def setUp(self):
        # Connect to the database and the address collection
        con = "mongodb+srv://django-microservice:<password>@<cluster>/?retryWrites=true&w=majority"
        client = MongoClient(con, server_api=ServerApi('1'))
        db = client["Subscription"]
        self.col = db["address_api_address"]
        # Determine the id of the last document
        for last in self.col.find().sort('id', -1).limit(1):
            self.__class__.last_id = last['id']

    # Happy path test creating an address
    def test_create_address(self):
        task_message = {"name": "A. Antovic",
                        "address": "Down Under 1",
                        "postalcode": "ZPT 17",
                        "city": "Gotham",
                        "country": "Northland",
                        "email": "antovic@upside.com"
                        }
        match_address_task.delay(task_message)

        sleep(2)

        for last in self.col.find().sort('id', -1).limit(1):
            self.assertEqual(last['name'], 'A. Antovic')
            self.col.delete_one({'id': last['id']})

    # Happy path tests matching mechanism
    def test_matching_mechanism(self):
        # Step 1: Add a new unique address that becomes a base address
        task_message = {"name": "B. Base",
                        "address": "Basement Road 71",
                        "postalcode": "ZPT 17",
                        "city": "Gotham",
                        "country": "Northland",
                        "email": "base@upside.com"
                        }
        match_address_task.delay(task_message)

        sleep(2)  # Wait for the task to finish

        # Check the base address and store data for later assertion
        for last in self.col.find().sort('id', -1).limit(1):
            self.assertEqual(last['name'], 'B. Base')
            self.__class__.base_id = last['id']
            self.__class__.base_street = last['address']

        # Step 2: Add a new address (variant) with a street that diverts slightly from the base address from step 1
        task_message = {"name": "V. Variant",
                        "address": "beasement road 71",
                        "postalcode": "ZPT 17",
                        "city": "Gotham",
                        "country": "Northland",
                        "email": "variant@upside.com"
                        }
        match_address_task.delay(task_message)

        sleep(2)  # Wait for the task to finish

        # Check the variant address and store data for later assertion
        for last in self.col.find().sort('id', -1).limit(1):
            self.assertEqual(last['name'], 'V. Variant')
            self.__class__.variant_id = last['id']
            self.__class__.variant_street = last['address']

        # Step 3: Check with an assertion that the last added address has the same street as the base address
        self.assertEqual(self.__class__.variant_street, self.__class__.base_street)

        # Step 4: Delete the added base address and variant
        self.col.delete_one({'id': self.__class__.base_id})
        self.col.delete_one({'id': self.__class__.variant_id})

    # Boundary tests
    def test_postalcode_too_long(self):
        task_message = {"name": "B. Berlin",
                        "address": "Down Under 1",
                        "postalcode": "Y23456789012345678901",
                        "city": "Gotham",
                        "country": "Northland",
                        "email": "berlin@upside.com"
                        }
        match_address_task.delay(task_message)

        sleep(2)

        for last in self.col.find().sort('id', -1).limit(1):
            self.assertEqual(last['id'], self.__class__.last_id)

    def test_postalcode_max(self):
        task_message = {"name": "C. Cortez",
                        "address": "Down Under 1",
                        "postalcode": "X2345678901234567890",
                        "city": "Gotham",
                        "country": "Northland",
                        "email": "cortez@upside.com"
                        }
        match_address_task.delay(task_message)

        sleep(2)

        for last in self.col.find().sort('id', -1).limit(1):
            inserted_id = last['id']
            self.assertEqual(last['name'], 'C. Cortez')
            self.col.delete_one({'id': inserted_id})


class MailTest(unittest.TestCase):
    # Happy path test
    def test_send_email(self):
        send_email_task.delay("D. Dhozos", "Street 1", "dhozos@upside.com")

    # Error guessing test
    def test_empty_name(self):
        send_email_task.delay("", "Road 2", "empty@upside.com")
