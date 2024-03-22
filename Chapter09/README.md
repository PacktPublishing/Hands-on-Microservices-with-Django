### Chapter 9, Securing Microservices

#### Guidance
- `subscription_apis/subscription_apis/settings.py`: replace `<password>` and `<cluster>` with your MongoDB values.
- `subscription_celery/subscription_celery/settings.py`: replace `<password>` and `<cluster>` with your MongoDB values.
- `subscription_celery/subscription/.env`: replace `CLIENT_TOKEN=<JWT_TOKEN>` and `SERVICE_TOKEN=<JWT_TOKEN>` with your generated values.
- `generate_token.py`: replace `<key_phrase>` with your value.
