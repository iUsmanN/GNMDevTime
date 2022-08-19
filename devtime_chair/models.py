from django.db import models

# Create your models here.
# class Developer(models.Model):
#     name = models.CharField(max_length=50)

class Record(models.Model):
    time = models.DateTimeField()
    developer = models.CharField(max_length=50)