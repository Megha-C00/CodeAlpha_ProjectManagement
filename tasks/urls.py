from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create-project/', views.create_project, name='create_project'),
    path('create-task/', views.create_task, name='create_task'),
    path('update-task/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('add-comment/<int:task_id>/', views.add_comment, name='add_comment'),
]