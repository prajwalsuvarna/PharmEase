from django.db import models
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

class User(models.Model):
    user_id=models.IntegerField(primary_key=True)
    entity_id=models.IntegerField()
    user_name=models.CharField(max_length=100)
    emp_id=models.ForeignKey(EmpModel, on_delete=models.CASCADE)
    user_password=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)

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

