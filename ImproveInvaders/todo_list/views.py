from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserType, Sala, Task, StudentWork, EnrolledCourses
from .forms import UserTypeForm, SalaForm, TaskForm
import datetime

# Create your views here.

# Paginas Centrais

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    userType = UserType.objects.filter(user=request.user).first()
    userType = userType.userType

    if userType == "PROFESSOR":
        salas = Sala.objects.filter(professor=request.user)

        return render(request, "todo_list/index.html", {
            "message":"É um professor logado",
            "user_type":userType,
            "salas":salas
        })
    
    if userType == "ESTUDANTE":
        salas = EnrolledCourses.objects.get(student=request.user)
        salas = salas.courses.all()

        return render(request, "todo_list/index.html", {
            "message":"É um aluno logado",
            "user_type":userType,
            'salas':salas
        })

    return render(request, "todo_list/index.html", {
        "user_type":userType,
    })

# Paginas sobre salas

def create_room(request):
    userType = UserType.objects.get(user=request.user)
    userType = userType.userType
    if not request.user.is_authenticated or userType != "PROFESSOR":
        return redirect('login')
    
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            sala = form.save(commit=False)
            sala.professor = request.user
            sala.save()  
        return redirect('home')

    form = SalaForm
    return render(request, 'todo_list/create_room.html', {
        'form':form,
    })


def view_room(request, room_id):
    if not request.user.is_authenticated:
        return redirect('login')

    sala = Sala.objects.get(pk=room_id)
    tasks = Task.objects.all().filter(sala=sala)
    return render(request, 'todo_list/view_room.html', {
        "sala":sala,
        "tasks":tasks,
    })

def delete_room(request, room_id):
    room = Sala.objects.get(pk=room_id)
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user != room.professor:
        return redirect('home')

    room.delete()
    return redirect('home')

# Tasks

def create_task(request, room_id):
    roomTeacher = Sala.objects.get(id=room_id)
    roomTeacher = roomTeacher.professor
    
    if not request.user.is_authenticated or request.user != roomTeacher:
        return redirect('login')

    sala = Sala.objects.get(id=room_id)
    form = TaskForm
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.dataUpload = datetime.datetime.now()
            task.sala = sala
            task.save()
            return redirect('home') 


    return render(request, 'todo_list/create_task.html', {
        'sala':sala,
        'form':form
    })

def view_task(request, task_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    task = Task.objects.get(pk=task_id)
    return render(request, 'todo_list/view_task.html', {
        'task':task,
    })

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    sala = Sala.objects.get(pk=task.sala.id)
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user != sala.professor:
        return redirect('home')

    task.delete()
    return redirect('home')

    
# Area do Aluno

def search_room(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        room = Sala.objects.get(pk=request.POST.get('room_id'))
        if room:
            courses = EnrolledCourses.objects.get(student=request.user)
            courses.courses.add(room)
            courses.save()

    return redirect('home')
        



# Pefil do usuario

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
            if userType.userType == "ESTUDANTE":
                courses = EnrolledCourses(student=user)
                courses.save()

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




