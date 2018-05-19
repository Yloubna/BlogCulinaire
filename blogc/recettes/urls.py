from django.contrib import admin
from django.conf.urls import include, url
from . import views

app_name = 'recettes'

urlpatterns = [
    url(r'^recettes/', views.recettes, app_name),
]

