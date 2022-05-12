from django.db import models
 

import random
import string
import json
from uuid import uuid4

from accounts.models import Account






class Notification(models.Model):
    user =  models.ForeignKey(Account,related_name='user_notify', on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=True,null=True) 
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

 


    def __str__(self):
        return f"{self.user.username} "

class Bank(models.Model):
    acc_name = models.CharField(max_length=50,blank=True,null=True) 
    acc_num = models.CharField(max_length=50,blank=True,null=True)
    ty_pe = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.ty_pe} "




class Packages(models.Model):


    hours= models.IntegerField()   
    name = models.CharField(max_length=40)
    percent = models.IntegerField()
    min_amount = models.IntegerField(default=0)
    max_amount = models.IntegerField(default=0)
    ref_percent = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"








class Transactions(models.Model):
    user =  models.ForeignKey(Account,related_name='user_transactions', on_delete=models.CASCADE,null=True, blank=True)
    amount = models.IntegerField( blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True) 
    approved_date = models.DateTimeField(blank=True,null=True) 
    is_approved = models.BooleanField(default=False)
    status = models.CharField(max_length=40,default="pending") 
    trans_type = models.CharField(max_length=50)

    bank_details = models.ForeignKey(Bank,related_name='trans_bank', on_delete=models.CASCADE,blank=True,null=True)

    unique_u = models.CharField(max_length=30, blank=True,null=True,unique=True)

    def __str__(self):
        return f"{self.user.username} :  {self.trans_type}"








STATUS = (
    ("active","active"),
    ("inactive","inactive"),
    ("pending","pending"),
    ("completed","completed"),
)

class Investments(models.Model):

    user =  models.ForeignKey(Account, on_delete = models.CASCADE)
    amount_invested = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    end_date =  models.DateTimeField(blank=True,null=True)
    start_date =  models.DateTimeField(blank=True,null=True)
    status = models.CharField(max_length=40, choices=STATUS,default="inactive")
    amount_earn = models.IntegerField(default=0)
    package = models.ForeignKey(Packages,on_delete = models.CASCADE, related_name="pack" , blank=True, null=True)
 
    def __str__(self):
        return f"{self.user.username} :  {self.amount_invested}"



