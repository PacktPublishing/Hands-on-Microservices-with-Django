import json
import requests


# CREATE - address
address = {"name": "Neo",
           "address": "The Matrix",
           "postalcode": "",
           "city": "Zion",
           "country": "Everland",
           "email": "neo@hackers.com"
           }
response = requests.post('http://127.0.0.1:8000/api/v1/addresses/', data=address)
print('CREATE:', response.status_code)

# fetch id of the created address from the response for later reference
id = json.loads(response.text)['id']

# READ  - all addresses
response = requests.get('http://127.0.0.1:8000/api/v1/addresses/')
print(response.text)

# UPDATE > PUT - overwrite address
address = {"name": "Neo",
           "address": "The Matrix",
           "postalcode": "ONE 965",
           "city": "Zion",
           "country": "Foreverland",
           "email": "neo@hackers.com"
           }
response = requests.put(f'http://127.0.0.1:8000/api/v1/addresses/{id}/', data=address)
print('PUT:', response.status_code)

# UPDATE > PATCH - update single field
patch = {"email": "neo@thematrix.com"}
response = requests.patch(f'http://127.0.0.1:8000/api/v1/addresses/{id}/', data=patch)
print('PATCH:', response.status_code)

# READ - specific address
response = requests.get(f'http://127.0.0.1:8000/api/v1/addresses/{id}/')
print(response.text)

# DELETE - address
response = requests.delete(f"http://127.0.0.1:8000/api/v1/addresses/{id}/")
print('DELETE:', response.status_code)
