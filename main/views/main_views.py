from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'main/main.html')