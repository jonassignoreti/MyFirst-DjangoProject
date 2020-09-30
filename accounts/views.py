from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Welcome to the accounts' page")