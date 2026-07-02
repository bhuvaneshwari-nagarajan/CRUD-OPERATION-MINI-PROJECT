from django import forms
from app2.models import Grocery

class GroceryForm(forms.ModelForm):
	class Meta:
		model = Grocery
		fields = '__all__'