FROM python:3.11.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
WORKDIR /
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7000
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:7000"]
