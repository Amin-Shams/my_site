from django.urls import path
from . import views

urlpatterns = [
    path('', ),
    path('posts/', ),
    path('posts/<slug:slug>', ),
]

