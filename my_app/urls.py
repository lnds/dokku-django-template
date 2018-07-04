from django.contrib import admin
from django.urls import path, include

from my_app.views import DemoListView, DemoCreateView

urlpatterns = [
    path('', DemoListView.as_view(), name='home'),
    path('create/', DemoCreateView.as_view(), name='create'),
]
