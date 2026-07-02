from django.shortcuts import render,redirect
from app4.models import Banking
from app4.forms import BankingForm

def read(request):
	stu=Banking.objects.all()
	return render(request,'result.html',{'p':stu})
def insert(request):
	form=BankingForm()
	if request.method=="POST":
		form=BankingForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/result/')
	return render(request,'insert.html',{'form':form})

def delete(request,id):
	s=Banking.objects.get(id=id)
	s.delete()
	return redirect('/result/')
def update(request,id):
	stu=Banking.objects.get(id=id)
	if request.method=="POST":
		form=BankingForm(request.POST,instance=stu)
		if form.is_valid():
			form.save()
		return redirect('/result/')
	return render(request,'update.html',{'p':stu})

# Create your views here.

# Create your views here.
