from django.db import models
# Create your models here.
class payment(models.Model):
	dgmail=models.EmailField(max_length=100,blank=False)
	ugmail=models.EmailField(max_length=100,blank=False)
	pid=models.IntegerField(blank=False)
	size=models.CharField(max_length=100,blank=False)
	chestsize=models.IntegerField(blank=False)
	waistsize=models.IntegerField(blank=False)
	sleevelength=models.CharField(max_length=100,blank=False)
	shoulderlength=models.IntegerField(blank=False)
	neckdepth=models.IntegerField(blank=False)
	price=models.IntegerField(blank=False)
	name=models.CharField(max_length=100,blank=False)
	adress=models.TextField(max_length=100,blank=False)
	phoneno=models.IntegerField(blank=False)
	card_choices = ( ('Debitcard','Debitcard') , ('creditcard','creditcard')  )
	cardtype=models.CharField(max_length=100,blank=False,choices=card_choices)
	cardno=models.IntegerField(blank=False)
	cvv=models.IntegerField(blank=False)
	class Meta:
		db_table="opayment"







