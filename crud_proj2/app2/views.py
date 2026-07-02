from django.shortcuts import render,redirect
from app2.models import Grocery
from app2.forms import GroceryForm

def read(request):
	stu=Grocery.objects.all()
	return render(request,'result.html',{'s':stu})
def insert(request):
	form=GroceryForm()
	if request.method=="POST":
		form=Grocery(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'insert.html',{'form':form})
def delete(request,id):
	s=Grocery.objects.get(id=id)
	s.delete()
	return redirect('/result/')
def update(request,id):
	stu=Grocery.objects.get(id=id)
	if request.method=="POST":
		form=GroceryForm(request.POST,instance=stu)
		if form.is_valid():
			form.save()
		return redirect('/result/')
	return render(request,'update.html',{'s':stu})

# Create your views here.