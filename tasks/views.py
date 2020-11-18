from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'hw4/index.html', context)


def update(request):
    if request.method == 'POST':
        item = request.POST.get('updateItem')
        new_item = request.POST.get('item_new')
        if request.POST.get('completeItem') == '1':
            completed_new = True
        else:
            completed_new = False
        Todo.objects.filter(task=item).update(completed=completed_new)
        Todo.objects.filter(task=item).update(task=new_item)
        return redirect('index')
    else:
        item = request.GET.get('updateItem')
        if Todo.objects.get(task=item).completed:
            completed = "checked"
        else:
            completed = ""
        return render(request, 'hw4/update.html', {"item": item, "completed": completed})


def delete(request):
    if request.method == 'POST':
        task = request.POST.get('deleteItem')
        Todo.objects.filter(task=task).delete()
        return redirect('index')
    else:
        item = request.GET.get('deleteItem')
        return render(request, 'hw4/delete.html', {"item": item})


def add(request):
    if request.method == 'POST':
        task = request.POST.get('addItem')
        Todo.objects.create(task=task)
        return redirect('index')


def complete_task(request):
    if request.method == 'POST':
        task = request.POST.get('completeItem')
        Todo.objects.filter(task=task).update(completed=True)
        return redirect('index')
