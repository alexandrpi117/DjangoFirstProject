from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def show_tasks(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/tasks.html', {'title': 'Main Page', 'tasks': tasks})


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Данные формы некорректны'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create-task.html', context)