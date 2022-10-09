from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserTypeForm
from .models import UserType

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, "todo_list/login.html", {})

    userType = UserType.objects.get(user=request.user)
    userType = userType.userType
    if userType == "PROFESSOR":
        return render(request, "todo_list/index.html", {
            "message":"É um professor logado",
        })
        
    return render(request, "todo_list/index.html", {})


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        password_confirm = request.POST.get('senha_confirm')

        user = User.objects.filter(username = username).first()

        if user:
            return render(request, "todo_list/cadastro.html", {
            "message":"Username já está sendo usado.",
        })   

        if not password == password_confirm:
            return render(request, "todo_list/cadastro.html", {
            "message":"As senhas não batem",
        })   

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        form = UserTypeForm(request.POST)
        if form.is_valid:
            userType = form.save(commit=False)
            userType.user = user
            userType.save()
            return render(request, "todo_list/cadastro.html", {
                "sucess_message":"Usuário cadastrado com sucesso!",
            })


    types = UserTypeForm
    return render(request, "todo_list/cadastro.html", {
        'form':types,
    })

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect("home")

        return render(request, "todo_list/login.html", {
            'warning':'Usuário ou senha incorretos.'
        })
        

    return render(request, "todo_list/login.html", {})


def logout(request):
    logout_django(request)
    return render(request, "todo_list/login.html", {
        "message":"Log out"
    })


