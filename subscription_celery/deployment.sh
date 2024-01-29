#!/bin/sh

# Set execute permission for this script:
# $ chmod +x deployment.sh
# Run this script:
# $ ./deployment.sh

# Deploy Django subscription app, Redis, Celery workers, and RESTful API

docker stop subscription_app 
docker stop address-api 
docker stop celery_worker 
docker stop redis_celery 

docker rm subscription_app 
docker rm address-api 
docker rm celery_worker 
docker rm redis_celery 

docker rmi subscription_celery-web 
docker rmi address-api 
docker rmi subscription_celery-worker 

docker compose up -d 
docker build . -t address-api-img
docker run --name address-api --network subscription_celery_default -d address-api-img
