from django.urls import path
from . import views


# url conf module

urlpatterns = [path('hello/',views.say_hello), path('time/', views.hello_and_time)]