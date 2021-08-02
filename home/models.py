from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12,default=None)
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    subscriber_email = models.EmailField(max_length=50)

    def __str__(self):
        return self.subscriber_email

class Dish(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='dish/')
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name