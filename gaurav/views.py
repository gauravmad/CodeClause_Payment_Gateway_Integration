from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data={
        'name':"Gaurav"
    }
    return render(request,"index.html",data)