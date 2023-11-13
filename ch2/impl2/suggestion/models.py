from django.db import models


class LogItem(models.Model):
    message = models.TextField()
    system = models.CharField(max_length=20, default="suggestion")
