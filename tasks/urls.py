from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('add', views.home, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('delete', views.deleteTodo, name='delete'),


]
