from django import forms
from .models import bag
class bagform(forms.ModelForm):
	class Meta:
		model=bag
		exclude = ('gmail','pid',)
		labels = {
		'chestsize' : "Chest Size",
		'waistsize':"Waist Size",
		'sleevelength':"Sleeve length",
		'shoulderlength':"Shoulder length",
		'neckdepth':"Neck Depth"
		}