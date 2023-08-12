from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name = 'homepage'),
    path('submit_task/', views.submit_task, name = 'submit_taskpage'),
    path('show_task/', views.show_task, name= 'show_taskpage'),
    path("edit_task/<int:id> ", views.edit_task, name= 'edit_taskpage'),
    path("delete_task/<int:id> ", views.Delete_task, name= 'delete_taskpage'),
    
    path("complete_task/<int:id> ", views.complete_task, name='complete_taskpage'),
    path("show_complete_task/", views.Show_complete_task, name= 'show_complete_taskpage'),
        
]
