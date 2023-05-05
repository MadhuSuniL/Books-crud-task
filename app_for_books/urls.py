from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('',IndexView),
    path('get_create_book',FirstView.as_view()),
    path('update_delete_book/<int:pk>',SecondView.as_view()),
]