from django import forms
from app5.models import Library
class LibraryForm(forms.ModelForm):
	class Meta:
		model = Library 
		fields= '__all__'