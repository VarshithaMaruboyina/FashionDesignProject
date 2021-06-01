from django import forms
from .models import payment
class paymentform(forms.ModelForm):
	class Meta:
		model=payment
		exclude = ('dgmail','ugmail','pid','size','chestsize','waistsize','sleevelength','shoulderlength','neckdepth','price')
	