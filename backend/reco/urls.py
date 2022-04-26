from django.urls import path

from . import views

app_name = 'reco'

urlpatterns = [
   path('',views.main, name='main')
]