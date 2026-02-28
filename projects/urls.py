from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('view/<int:pk>/', views.project_view, name='project_view'),
]