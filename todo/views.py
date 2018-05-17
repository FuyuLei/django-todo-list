from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoModelFrom


def index(request):
    todos = Todo.objects.all()  # select * from
    return render(request, 'todo/index.html', {'todos': todos})

def new(request):
    form = TodoModelFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:index')

    return render(request, 'todo/new.html', {'form': form})