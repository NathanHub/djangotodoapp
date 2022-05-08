from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name='index'),
    path('add', views.add_todo_item_view, name='add'),
    path('completed/<todo_id>', views.completed_todo, name='completed'),
    path('deletecompleted', views.delete_completed_view, name='deletecompleted'),
    path('deleteall', views.delete_all_view, name='deleteall')
]
