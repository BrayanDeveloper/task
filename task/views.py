from django.shortcuts import render, redirect
from task.models import Task
# Create your views here.


def home(request):
    return render(request, 'task/home.html')

def task(request):
    statement = Task.objects.all()
    context = {'statement': statement}
    return render(request, 'task/task.html', context)

def editTask(request):
    if request.method == "GET":
        statement = Task.objects.filter(id=request.GET.get('id'))
        context = {'statement': statement}
        return render(request, 'task/edit_task.html', context)

def editTaskFull(request):
    if request.method == "POST":
        Task.objects.filter(id=request.POST.get('id')).update(task=request.POST.get('task'), category=request.POST.get('category'), date_init=request.POST.get('date_init'), date_finish=request.POST.get('date_finish'), state=request.POST.get('state'))
        return redirect('/task')

