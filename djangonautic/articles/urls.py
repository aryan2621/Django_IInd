from django.contrib import admin
from django.urls import path

# routes
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.article_details, name='detail')
]
