from django.db import models
# Create your models here.

class User(models.Model):
    user_id=models.IntegerField(primary_key=True)
    entity_id=models.IntegerField()
    user_name=models.CharField(max_length=100)
    emp_id=models.IntegerField()
    user_password=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    
class EmpModel(models.Model):
    empname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    e_id=models.IntegerField(primary_key=True)
    mobile=models.IntegerField()
    class Meta:
        db_table="employee"

