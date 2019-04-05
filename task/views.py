from django.shortcuts import render, redirect
from task.models import Task
# Create your views here.


def home(request):
    return render(request, 'task/home.html')

def task(request):
    statement = Task.objects.all().order_by('-id')[:5]
    context = {'statement': statement}
    return render(request, 'task/task.html', context)

def taskAll(request):
    statement = Task.objects.all().order_by('-id')
    context = {'statement': statement}
    return render(request, 'task/task_all.html', context)

def editTask(request):
    if request.method == "GET":
        statement = Task.objects.filter(id=request.GET.get('id'))
        context = {'statement': statement}
        return render(request, 'task/edit_task.html', context)

def editTaskFull(request):
    if request.method == "POST":
        Task.objects.filter(id=request.POST.get('id')).update(task=request.POST.get('task'), category=request.POST.get('category'), date_init=request.POST.get('date_init'), date_finish=request.POST.get('date_finish'), state=request.POST.get('state'))
        return redirect('/task')

def addTask(request):
    if request.method == "POST":
        statement = Task(task=request.POST.get('task'), category=request.POST.get('category'), date_init=request.POST.get('date_init'), date_finish=request.POST.get('date_finish'), state=request.POST.get('state'))
        statement.save()
        return redirect('/task/')
    return render(request, 'task/add_task.html')

def deleteTask(request):
    if request.method == "GET":
        delete = Task.objects.filter(id=request.GET.get('id')).delete()
        return redirect('/task')
    return redirect('/task')

def searchTask(request):
    if request.method == "POST":
        filter = Task.objects.filter(task__contains=request.POST.get('task'))
        context = {'filter':filter}
        return render(request, 'task/search_task.html', context)
    return redirect('/task')

def stateTask(request):
    if request.method == "GET":
        Task.objects.filter(id=request.GET.get('id')).update(state=request.GET.get('state'))
        return redirect('/task')