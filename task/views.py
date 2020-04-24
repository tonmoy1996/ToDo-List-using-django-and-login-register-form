from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
# Create your views here.

#profile
@login_required(login_url='login')
def Profile(request):
    return render(request, 'profile.html')
#loginform
def LoginForm(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "username or password is not correct" )
            return redirect('login')


    
    return render(request ,'login.html')

#logout
def UserLogout(request):
    logout(request)
    return redirect('login')

#User Form
def CreateUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form=CreateUserForm()
        if request.method == "POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Login successful " + user )
                return redirect('login')
        context={'form':form}
        return render(request, "createuser.html",context)


def index(request):

    tasks=Task.objects.all()
    form= TaskForm()
    if request.method== 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')

    context={
        'tasks': tasks,
        'forms': form
    }

    return render(request,'tasks/list.html',context)


def deletetask(request, pk):
    val=Task.objects.get(id=pk)
    
    if request.method == 'POST':
        Task.objects.filter(id=pk).delete()
        
        
        return redirect('/')
    

    context={'tasks': val}

    return render(request, 'tasks/delete.html',context)

def update(request, pk1):

    task= Task.objects.get(id=pk1)
    print(task)
    form=TaskForm(instance=task)
    
    if request.method == 'POST':
        form= TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'forms':form}

    return render(request, 'tasks/update.html',context)