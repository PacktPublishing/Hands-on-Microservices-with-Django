#!/bin/sh

# Set execute permission for this script:
# $ chmod +x deployment.sh
# Run this script:
# $ ./deployment.sh

# Deploy Django subscription app, Redis, and Celery workers

# Stopping containers 
docker stop subscription_app 
docker stop celery_worker 
docker stop redis_celery 
# Removing containers 
docker rm subscription_app 
docker rm celery_worker 
docker rm redis_celery 
# Removing images 
docker rmi subscription_celery-web 
docker rmi subscription_celery-worker 
# Recreate images and containers 
docker compose up -d 

# Deploy RESTful API
docker stop address-api 
docker rm address-api 
docker rmi address-api-img
cd ..
cd subscription_apis
docker build . -t address-api-img
docker run --name address-api --network subscription_celery_default -d -p 7000:7000 address-api-img
