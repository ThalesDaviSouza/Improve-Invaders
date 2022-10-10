from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('sobre/', views.sobre, name='sobre'),
    
    # Room
    path('create_room/', views.create_room, name='create-room'),
    path('view_room/<room_id>', views.view_room, name='view-room'),
    path('delete_room/<room_id>', views.delete_room, name='delete-room'),
    path('list_room/', views.list_room, name='list-room'),
    
    # Task
    path('create_task/<room_id>', views.create_task, name='create-task'),
    path('view_task/<task_id>', views.view_task, name='view-task'),
    path('delete_task/<task_id>', views.delete_task, name='delete-task'),
    
    # Area do aluno
    path('search_room/', views.search_room, name='search-room'),
    path('todo/', views.todo, name='todo'),
    path('send_task/<task_id>', views.send_task, name='send-task'),



    # Oq tenho q acrescentar
    # path('shop/'),
]