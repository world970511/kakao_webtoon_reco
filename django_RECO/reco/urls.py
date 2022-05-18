from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'reco'

urlpatterns = [
   path('',views.intro,name='intro'),
   path('select/',views.select,name='select'),
   path('result/',views.result,name='result')
]
