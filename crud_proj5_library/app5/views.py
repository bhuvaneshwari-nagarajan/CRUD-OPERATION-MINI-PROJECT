from django.shortcuts import render, redirect
from app5.models import Library
from app5.forms import LibraryForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            return render(request, "login.html", {
                "error": "Invalid Username"
            })

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/result/')
        else:
            return render(request, "login.html", {
                "error": "Invalid Password"
            })

    # Page first time open ஆகும்போது
    return render(request, "login.html")

def read(request):
    stu = Library.objects.all()
    return render(request, 'result.html', {'p': stu})


def insert(request):
    form = LibraryForm()
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/result/')
    return render(request, 'insert.html', {'form': form})

def update(request, id):
    p = Library.objects.get(sno=id)

    if request.method == "POST":
        p.book_name = request.POST["book_name"]
        p.author_name = request.POST["author_name"]
        p.publisher = request.POST["publisher"]
        p.price = request.POST["price"]
        p.quantity = request.POST["quantity"]
        p.available_copies = request.POST["available_copies"]
        p.language = request.POST["language"]
        p.shelf_no = request.POST["shelf_no"]
        p.issue_date = request.POST["issue_date"]
        p.return_date = request.POST["return_date"]

        p.save()
        return redirect('/result/')

    return render(request, "update.html", {'p': p})

def delete(request, id):
    s = Library.objects.get(sno=id)
    s.delete()
    return redirect('/result/')
   