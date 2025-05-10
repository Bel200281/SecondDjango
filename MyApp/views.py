from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """
    <h1>Тут будет список:</h1>
    """

    return HttpResponse(text)


