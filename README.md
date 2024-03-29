### Welcome to the repository for the book *Hands-On Microservices with Django*.
![](https://github.com/PacktPublishing/Hands-on-Microservices-with-Django/blob/main/9781835468524.jpg)
The book [*Hands-On Microservices with Django*](https://www.packtpub.com/product/hands-on-microservices-with-django/9781835468524) teaches you how to develop scalable applications with Django microservices using community-standard components like Celery, Redis, RabbitMQ, and Docker. This repository contains the corresponding code samples.

#### Prerequisites
To run the code in this repository, you need the following:
- Linux/MacOS/Windows 10/11 & [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) because Celery doesn't run on Windows.
- [Python 3.11](https://www.python.org/downloads/) or later.
- The Python packages from this [requirements.txt](https://github.com/PacktPublishing/Hands-on-Microservices-with-Django/blob/main/ch8/subscription_celery/requirements.txt).
- [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- [Redis](https://redis.io/docs/install/install-stack/docker/) (running as a Docker container).
- [RabbitMQ](https://www.rabbitmq.com/docs/download) (running as a Docker container).

#### Extra for WSL
If you're on WSL, run the following commands to ensure Python works correctly:  
1. `$ sudo apt update && sudo apt upgrade`  
1. `$ sudo apt upgrade python3`  
1. `$ sudo apt install python3-pip`  
1. `$ sudo apt install python3-venv`  
