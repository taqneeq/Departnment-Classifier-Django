from django.shortcuts import render, redirect
from website.form import get_department  # Replace with the actual path to your Python function
import pickle
import pandas as pd
import json

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def form(request):
    return render(request, 'website/form.html')

def result(request):
    if request.method == 'POST':
        output = request.POST.get('modeldata')
        data = json.loads(output)

        print("Received data:", data)  # Add this line for debugging

        if all(x == 1 for x in data):
            return redirect('http://www.youtube.com/watch?v=dQw4w9WgXcQ', code=302)
        elif all(x == 5 for x in data):
            return render(request, 'website/result.html', {'department': "SUPER CORE APPLICATIONS ARE CLOSED"})

        prediction = get_department(data=data)
        return render(request, 'website/result.html', {'department': prediction.upper()})
