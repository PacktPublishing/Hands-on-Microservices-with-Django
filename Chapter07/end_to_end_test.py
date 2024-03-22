import unittest
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class SubscriptionTest(unittest.TestCase):
    def setUp(self):
        # Selenium
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://127.0.0.1:8000/subscription/")
        self.assertIn('Subscription', self.driver.title)

        # MongoDB
        con = "mongodb+srv://django-microservice:<password>@<cluster>/?retryWrites=true&w=majority"
        client = MongoClient(con, server_api=ServerApi('1'))
        db = client["Subscription"]
        self.col = db["address_api_address"]

    def test_create_subscription(self):
        driver = self.driver
        col = self.col

        # Enter subscription address
        driver.find_element(By.NAME, "name").send_keys("S. Selenium")
        driver.find_element(By.NAME, "address").send_keys("Earth avenue 301")
        driver.find_element(By.NAME, "postalcode").send_keys("GALX 7")
        driver.find_element(By.NAME, "city").send_keys("Rockdale")
        driver.find_element(By.NAME, "country").send_keys("everland")
        driver.find_element(By.NAME, "email").send_keys("sel@earth.com")
        driver.find_element(By.NAME, "subscribe_button").click()

        # Check Success page
        sleep(2) # Wait for the microservices to finish
        success_header = driver.find_element(By.NAME, "success_header").text
        self.assertIn("Thanks!", success_header)

        # Ensure the address was added
        for last in col.find().sort('id', -1).limit(1):
            self.assertEqual(last['name'], 'S. Selenium')
            col.delete_one({'id': last['id']})

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
