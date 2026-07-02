from django.shortcuts import render,redirect
from app3.models import Product
from app3.forms import ProductForm

def read(request):
	stu=Product.objects.all()
	return render(request,'result.html',{'p':stu})
def insert(request):
	form=ProductForm()
	if request.method=="POST":
		form=ProductForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/result/')
	return render(request,'insert.html',{'form':form})

def delete(request,id):
	s=Product.objects.get(id=id)
	s.delete()
	return redirect('/result/')
def update(request,id):
	stu=Product.objects.get(id=id)
	if request.method=="POST":
		form=ProductForm(request.POST,instance=stu)
		if form.is_valid():
			form.save()
		return redirect('/result/')
	return render(request,'update.html',{'p':stu})

# Create your views here.

# Create your views here.
