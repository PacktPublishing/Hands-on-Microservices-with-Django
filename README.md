# Hands-On Microservices with Django

This is the code repository for the book [Hands-On Microservices with Django](https://www.packtpub.com/product/hands-on-microservices-with-django/9781835468524), published by Packt.

## What is this book about?
<a href="https://www.packtpub.com/product/hands-on-microservices-with-django/9781835468524"><img src="https://content.packt.com/B22012/cover_image_small.jpg" alt="Book Name" height="256px" align="right"></a>
Are you a Django developer looking to leverage microservices to create optimized and scalable web applications? If yes, then this book is for you. With microservices, you can split an application into self-contained services, each with a specific scope running asynchronously while collectively executing processes. Written by an experienced Python developer, *Hands-On Microservices with Django* teaches you how to develop and deploy microservices using Django and accompanying components such as Celery and Redis.

This book covers the following features:
* Understand the architecture of microservices and how Django implements it
* Build microservices that leverage community-standard components such as Celery, RabbitMQ, and Redis
* Test microservices and deploy them with Docker
* Enhance the security of your microservices for production readiness
* Boost microservice performance through caching
* Implement best practices to design and deploy high-performing microservices

Get your [copy](https://www.amazon.com/Hands-Microservices-Django-cloud-native-applications-ebook/dp/B0CW1JN916/ref=sr_1_3?crid=K4LJ2H6WTXYO&dib=eyJ2IjoiMSJ9.TpLeLks_HmBHFmPdbtNnUdzLF-UXtCVUODw0HBAYLHo8qVb9XA_mZLak4UWtsM5mpBoUlOSCeQKFPyoj5wvA_i2qLeu9nhafvczf3PhCUDo.QeyEr3c8ab_jq3bdwn3dD8gMziMlbt4c_ZQ2uOwCYKg&dib_tag=se&keywords=Hands-On+Microservices+with+Django&qid=1711916487&s=books&sprefix=hands-on+microservices+with+django%2Cstripbooks%2C247&sr=1-3).

## Instructions and Navigations
The code is organized into folders and looks like the following:
```Python
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
```

### What you need for this book
This book is for Django developers who want to take the next step in back-end application development by adopting cloud-native microservices. Backend developers with working knowledge of Flask or other Python programming web frameworks will also benefit from this book. Basic knowledge of developing web APIs will help you get started with quickly building microservices on your own.

## Software and Operating System List
With the following software and operating system list you can run all code files present in the book (Chapters 2-11):
| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 2-11        | Django                     | Windows & Windows Subsystem for Linux (WSL)*, Mac OS, or Linux |
| 2-11        | Redis            |  |
| 2-11        | RabbitMQ            |  |
| 2-11        | Celery            |  |
| 2-11        | MongoDB Cloud version            |  |
* Celery only runs on Mac OS or Linux, so if you are on Windows, you will need WSL.

### Extra for WSL
If you're on WSL, run the following commands to ensure Python works correctly:  
1. `$ sudo apt update && sudo apt upgrade`  
1. `$ sudo apt upgrade python3`  
1. `$ sudo apt install python3-pip`  
1. `$ sudo apt install python3-venv`

## Get to Know the Author
**Tieme Woldman** works as a freelance Python developer and technical writer. As a Python developer, he builds web and data engineering applications with Django and Python data transformation packages such as pandas. As a technical writer, he has written software and user documentation for software companies such as Instruqt, Noldus Information Technology, and Rulecube. Tieme lives in the Netherlands, has a bachelor's degree in computer science, and holds several (technical) writing certifications.
