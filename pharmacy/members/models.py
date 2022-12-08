from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
    
class EmpModel(models.Model):
    empname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    e_id=models.IntegerField(primary_key=True)
    mobile=models.BigIntegerField()
    class Meta:
        db_table="employee"
    def __str__(self):
        return self.empname

class Users(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_id=models.OneToOneField(EmpModel, on_delete=models.CASCADE)
    class Meta:
        db_table="Users"
    def __str__(self):
        return self.user.username


class DistModel(models.Model):
    dist_id=models.IntegerField(primary_key=True)
    dist_name=models.CharField(max_length=100)
    d_email= models.EmailField(max_length = 254)
    d_pno=models.BigIntegerField()
    class Meta:
        db_table="Distributor"
    def __str__(self):
        return self.dist_name
    

class DrgModel(models.Model):
    dg_id=models.IntegerField(primary_key=True)
    dgname=models.CharField(max_length=100)
    stock=models.IntegerField()
    dist_id = models.ForeignKey(DistModel, on_delete=models.CASCADE)
    price=models.IntegerField()
    class Meta:
        db_table="Drugs"
    def __str__(self):
        return self.dgname
    def __iter__(self):
        return iter(self.dgname)

class Bill(models.Model):
    sale_id=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    phone_no=models.BigIntegerField()
    stock=models.IntegerField()
    age=models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)
    drg_id=models.ManyToManyField(DrgModel)
    amt=models.BigIntegerField(null=True)
    emp_name=models.CharField(max_length=100,null=True)
    class Meta:
        db_table="Bill"
    def __str__(self):
        return self.cname


