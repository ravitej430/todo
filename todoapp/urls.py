from django.urls import path
from. import views
from django.contrib import admin


urlpatterns = [
    path('todoapp/',views.todoapp),
    path('addtodoitems/',views.addTodoView),
    path('deleteTodoItems/<int:i>/', views.deleteTodoView)
]
