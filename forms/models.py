from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length = 62)
    email = models.CharField(max_length=62)
    number = models.CharField(max_length=13)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.fullname}"

class Digital(models.Model):
    fullname = models.CharField(max_length = 62)
    username = models.CharField(max_length = 62)
    email = models.CharField(max_length = 62)
    number = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    address = models.CharField(max_length = 62)
    occupation = models.CharField(max_length = 62)
    whatsapp = models.CharField(max_length = 62)
    facebook = models.CharField(max_length = 62)
    instagram = models.CharField(max_length = 62)
    twitter = models.CharField(max_length = 62)
    linkedin = models.CharField(max_length = 62)

    def __str__(self):
        return f"{self.fullname}"

class SME(models.Model):
    fullname = models.CharField(max_length = 62)
    brandname = models.CharField(max_length = 62)
    email = models.CharField(max_length = 62)
    number = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    category = models.CharField(max_length = 62)
    address = models.CharField(max_length = 62)
    occupation = models.CharField(max_length = 62)
    whatsapp = models.CharField(max_length = 62)
    facebook = models.CharField(max_length = 62)
    instagram = models.CharField(max_length = 62)
    twitter = models.CharField(max_length = 62)
    linkedin = models.CharField(max_length = 62)

    def __str__(self):
        return f"{self.fullname}"

class Coupon(models.Model):
    fullname = models.CharField(max_length = 62)
    username = models.CharField(max_length = 62)
    email = models.CharField(max_length = 62)
    number = models.CharField(max_length = 15)
    country = models.CharField(max_length = 62)
    state = models.CharField(max_length = 62)
    city = models.CharField(max_length = 62)
    address = models.CharField(max_length = 62)
    occupation =models.CharField(max_length = 62)
    idno = models.CharField(max_length = 62)
    utility = models.CharField(max_length = 62)
    bvn = models.CharField(max_length = 62)
    whatsapp = models.CharField(max_length = 62)
    facebook = models.CharField(max_length = 62)
    instagram = models.CharField(max_length = 62)
    twitter = models.CharField(max_length = 62)
    linkedin = models.CharField(max_length = 62)

    def __str__(self):
        return f"{self.fullname}"

class Vocation(models.Model):
    fullname = models.CharField(max_length = 62)
    username = models.CharField(max_length = 62)
    email = models.CharField(max_length = 62)
    number = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    address = models.CharField(max_length = 62)
    field = models.CharField(max_length = 62)
    whatsapp = models.CharField(max_length = 62)
    facebook = models.CharField(max_length = 62)
    instagram = models.CharField(max_length = 62)
    twitter = models.CharField(max_length = 62)
    linkedin = models.CharField(max_length = 62)

    def __str__(self):
        return f"{self.fullname}"

class Influencer(models.Model):
    fullname = models.CharField(max_length = 62)
    username = models.CharField(max_length = 62)
    email = models.CharField(max_length = 62)
    number = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    address = models.CharField(max_length = 62)
    occupation = models.CharField(max_length = 62)
    whatsapp = models.CharField(max_length = 62)
    facebook = models.CharField(max_length = 62)
    instagram = models.CharField(max_length = 62)
    twitter = models.CharField(max_length = 62)
    linkedin = models.CharField(max_length = 62)

    def __str__(self):
        return f"{self.fullname}"