from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book, name='book'),
    path('inquiry/', views.inquiry, name='inquiry'),
]