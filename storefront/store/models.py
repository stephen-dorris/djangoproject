from django.db import models
from django.db.models.base import Model

# Create your models here.

class Product(models.Model):

   
    # Char Field has max len 255
    title = models.CharField(max_length=255)
    description = models.TextField()
    # use for money (ex if our max price is 9999.99)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    # updates everytime it is saved
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    ## CHOICE FIELD EXAMPLE (first element is stored second is human readable name)
    MEMBERSHIP_BRONZE_KEY = 'B'
    MEMBERSHIP_BRONZE_VAL = 'Bronze'
    MEMBERSHIP_SILVER_KEY = 'S'
    MEMBERSHIP_SILVER_VAL = 'Silver'
    MEMBERSHIP_GOLD_KEY = 'G'
    MEMBERSHIP_GOLD_VAL = 'Gold'

    MEMBERSHIP_CHOICES = [(MEMBERSHIP_BRONZE_KEY,MEMBERSHIP_BRONZE_VAL),
     (MEMBERSHIP_SILVER_KEY,MEMBERSHIP_SILVER_VAL), 
     (MEMBERSHIP_GOLD_KEY,MEMBERSHIP_GOLD_VAL) ]


    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE_KEY)



class Order:
    STATUS_PENDING_KEY = 'P'
    STATUS_PENDING_VAL = 'Pending'
    STATUS_COMPLETE_KEY = 'C'
    STATUS_COMPLETE_VAL = 'Complete'
    STATUS_FAILED_KEY = 'F'
    STATUS_FAILED_VAL = 'Failed'

    PAYMENT_STATUS_CHOICES =[(STATUS_PENDING_KEY,STATUS_PENDING_VAL),
     (STATUS_COMPLETE_KEY,STATUS_COMPLETE_VAL), 
     (STATUS_FAILED_KEY,STATUS_FAILED_VAL) ]
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES,default=STATUS_PENDING_KEY)

    placed_at = models.DateField(auto_now_add=True)