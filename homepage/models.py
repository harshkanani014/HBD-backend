from django.db import models

# Create your models here.

class usermodel(models.Model):
    fromm = models.TextField()
    to = models.TextField()
    message = models.TextField()
    hexx = models.TextField()
