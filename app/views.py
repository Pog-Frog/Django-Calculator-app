from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def get_equation(request):
    equation = request.GET['input']
    if "|" in equation:
        idx = equation.index("|")
        
    return HttpResponse(equation)
