from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def weather1(request, city, year):

    print(city)
    print(year)
    return HttpResponse('weather1')