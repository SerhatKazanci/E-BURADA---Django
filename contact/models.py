import email
from email import message
from operator import mod
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Follow(models.Model):

    phone = models.CharField(max_length=50)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.phone
