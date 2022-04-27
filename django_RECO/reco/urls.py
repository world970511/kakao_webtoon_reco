from django.urls import path

from . import views

app_name = 'reco'

urlpatterns = [
   path('',views.intro,name='intro'),
   path('select/',views.select,name='select')
]