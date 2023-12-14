from django.shortcuts import render, redirect
from website.form import get_department  # Replace with the actual path to your Python function
import pickle
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def form(request):
    return render(request, 'website/form.html')

def result(request):
    if request.method == 'POST':
        output = request.POST.get('modeldata')
        data = list(map(int, output.split(",")))

        if all(x == 1 for x in data):
            return redirect('http://www.youtube.com/watch?v=dQw4w9WgXcQ', code=302)
        elif all(x == 5 for x in data):
            return render(request, 'your_app_name/result.html', {'department': "SUPER CORE APPLICATIONS ARE CLOSED"})

        prediction = get_department(data=data)
        return render(request, 'your_app_name/result.html', {'department': prediction.upper()})
