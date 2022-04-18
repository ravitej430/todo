from django.shortcuts import render
from .models import TodoListItems
from django.http import HttpResponseRedirect


# Create your views here.
def todoapp(request):
    all_todo_items=TodoListItems.objects.all()
    return render(request,'todolist.html',
    {'all_items':all_todo_items})
    
def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItems(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 
    
def deleteTodoView(request, i):
    y = TodoListItems.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 

