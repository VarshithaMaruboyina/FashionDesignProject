from django.db import models

# Create your models here.
class dregister(models.Model):
	name=models.CharField(max_length=100,blank=False)
	gmail=models.EmailField(max_length=100,blank=False,primary_key=True)
	mobileno=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	imagefile = models.ImageField(upload_to='images/') 
	class Meta:
		db_table="dregister"

class designs(models.Model):
	name=models.CharField(max_length=100,blank=False)
	gmail=models.EmailField(max_length=100,blank=False)
	DesignName=models.CharField(max_length=100,blank=False,default='NULL',)
	design = models.ImageField(upload_to='designs/') 
	design_choices = ( ('partywear','partywear') , ('traditional','traditional')  )
	designtype=models.CharField(max_length=100,blank=False,choices=design_choices,default='NULL')
	price=models.IntegerField(blank=False,default=10)
	description=models.CharField(max_length=255,blank=False,default='NULL')
	class Meta:
		db_table="designs"