from django.urls import path
from . import views
urlpatterns = [
    path('task2/', views.getData),
    path('task3/', views.getDataTemplate),
]
