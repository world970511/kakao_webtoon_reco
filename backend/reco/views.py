from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from .serializers import AllDataSerializer
from .models import AllData

from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, '')