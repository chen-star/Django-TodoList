from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . import models


def todolist(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            models.Todo.objects.create(title=title)
    list = models.Todo.objects.all()
    return render(request, 'todolist.html', locals())



def delete(request, pk):
    todo = get_object_or_404(models.Todo, id=pk)
    todo.delete()
    return HttpResponseRedirect('/')



def complete(request, pk):
    todo = get_object_or_404(models.Todo, id=pk)
    todo.completed = True
    todo.save()
    return HttpResponseRedirect('/')