from django import forms
from app4.models import Banking
class BankingForm(forms.ModelForm):
	class Meta:
		model = Banking 
		fields= '__all__'