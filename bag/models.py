from django.db import models

# Create your models here.
class bag(models.Model):
	gmail=models.EmailField(max_length=100,blank=False)
	pid=models.IntegerField(blank=False)
	size_choice = ( ('S','S') , ('M','M') ,('L','L'),('XL','XL'),('XXL','XXL') )
	size=models.CharField(max_length=100,blank=False,choices=size_choice)
	chestsize=models.IntegerField(blank=False)
	waistsize=models.IntegerField(blank=False)
	sleeve_choice = ( ('sleeveless','sleeveless') , ('halfsleeves','halfsleeves') ,('fullsleeves','fullsleeves'),('petalsleeves','petalsleeves') )
	sleevelength=models.CharField(max_length=100,blank=False,choices=sleeve_choice)
	shoulderlength=models.IntegerField(blank=False)
	neckdepth=models.IntegerField(blank=False)
	class Meta:
		db_table="bag"
