from django.shortcuts import render
import base64
from io import BytesIO
from matplotlib import pyplot as plt
import pandas as pd

# Create your views here.
def problem1(request):
    df = pd.read_csv('austin_weather.csv')
    df = df.to_html()
    context = {
        'df': df
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    return render(request, 'weathers/problem2.html')

def problem3(request):
    return render(request, 'weathers/problem3.html')

def problem4(request):
    return render(request, 'weathers/problem4.html')