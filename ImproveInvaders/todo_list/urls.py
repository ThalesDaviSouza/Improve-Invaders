from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Home
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    
    # Room
    path('create_room/', views.create_room, name='create-room'),
    path('view_room/<room_id>', views.view_room, name='view-room'),
    path('delete_room/<room_id>', views.delete_room, name='delete-room'),
    
    # Task
    path('create_task/<room_id>', views.create_task, name='create-task'),
    path('view_task/<task_id>', views.view_task, name='view-task'),
    path('delete_task/<task_id>', views.delete_task, name='delete-task'),
    
    # Area do aluno
    path('search_room/', views.search_room, name='search-room'),
    # Oq tenho q acrescentar
    # path('todo_list')
    # path('info/')
]