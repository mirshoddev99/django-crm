from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
