from django import forms
from .models import dregister,designs

class dregisterform(forms.ModelForm):
	class Meta:
		model=dregister
		fields="__all__"


class dloginform(forms.Form):
	gmail=forms.EmailField(max_length=100)
	password=forms.CharField(max_length=100)


class designsform(forms.ModelForm):
	class Meta:
		model=designs
		exclude = ('name','gmail',)
		labels = {
		'design' : "upload your design",
		'DesignName':"enter the name of your design",
		}