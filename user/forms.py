from django import forms
from .models import uregister


class uregisterform(forms.ModelForm):
	class Meta:
		model=uregister
		fields="__all__"

class uloginform(forms.Form):
	gmail=forms.EmailField(max_length=100)
	password=forms.CharField(max_length=100)