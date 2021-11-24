from django.urls import path
from .views import main_views

app_name ='main'

urlpatterns = [
      path('', main_views.index, name='index'),
]