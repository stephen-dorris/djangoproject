from django.urls import path
from . import views


# url conf module

urlpatterns = [path('say_hello/',views.say_hello), path('say_time/', views.hello_and_time)]