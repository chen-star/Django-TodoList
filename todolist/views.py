from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime

class Todo:
    def __init__(self, description, isCompleted):
        self.description = description
        self.isCompleted = isCompleted


def todolist(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            Todo.objects.create(title=title)

    todolist = Todo.objects.all()
    return render(request, '/templates/index.html', locals())



def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return HttpResponseRedirect('/')



def complete(request):
    todo = get_object_or_404(Todo, id=pk)
    todo.completed = True
    todo.save()
    return HttpResponseRedirect('/')