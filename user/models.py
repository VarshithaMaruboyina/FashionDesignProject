from django.db import models

class uregister(models.Model):
	name=models.CharField(max_length=100,blank=False)
	gmail=models.EmailField(max_length=100,blank=False,primary_key=True)
	mobileno=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table="uregister"
# Create your models here.
