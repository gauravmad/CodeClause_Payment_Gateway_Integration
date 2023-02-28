from django.http import HttpResponse
from django.shortcuts import render,redirect


def home(request):
    data={
        'name':"Gaurav"
    }
    return render(request,"index.html",data)

def paymentsuccess(request):
    if request.method == "POST":
        transaction_id = request.POST.get('transaction_id')
        transaction_status = request.POST.get('transaction_status')
    return render(request,"ordersuccess.html")