from django.shortcuts import render
from .models import AllData

# Create your views here.
def intro(request):
    return render(request, 'intro.html')

#여기부터 작성할 것
def select(request):
    return render(request, 'select.html')