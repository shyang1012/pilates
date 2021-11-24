from django.urls import path
from .views import base_views

app_name ='board'

urlpatterns = [
    path('', base_views.list, name='list'),
]