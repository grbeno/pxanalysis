from django.urls import path
from .views import firstTest

urlpatterns = [path("",firstTest,name="home"),]