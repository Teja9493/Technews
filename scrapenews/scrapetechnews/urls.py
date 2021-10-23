
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('scrapetechnews/technews',views.technews,name="technews"),
]
