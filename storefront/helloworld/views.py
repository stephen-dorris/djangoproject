from django.shortcuts import render
from django.http import HttpResponse
import datetime



# Simple Hello World
def say_hello(request):
    return HttpResponse("Hello World")


# Uses template to show different response based on time. 
def hello_and_time(request):
    time = datetime.datetime.now()
    # Response Types 
    base_template = {'name': 'Stephen', 'time': str(time) }
    num_options_in_template = 4

    mod_ = time.microsecond % num_options_in_template

    # both name and time
    if mod_ == 0:
        return render(request,'time_of_day.html',base_template)
    # just name
    elif mod_ == 1:
        return render(request, 'time_of_day.html', {'name' : base_template['name']})
    
    # just time
    elif mod_ == 2:
        return render(request, 'time_of_day.html', {'time' : base_template['time']})
    # empty 
    else:
        return render(request, 'time_of_day.html', {})

