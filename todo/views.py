from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import ToDo

# Create your views here.

def index(request):
    todos = ToDo.objects.all()
    return render(request,"index.html",{"todos":todos})

def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = ToDo(title=title,completed=False)
        newTodo.save()
        return redirect("/")

def update(request,id):
    todo = get_object_or_404(ToDo,id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("/")

def delete(request,id):
    todo = get_object_or_404(ToDo,id=id)
    todo.delete()
    return redirect("/")