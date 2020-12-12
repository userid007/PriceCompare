from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .price_comp import *


# Create your views here.


def home(request):
    return render(request, 'compare/index.html', {})


def result(request):
    if request.method == 'GET':
        return redirect('home')
    elif request.method == 'POST':
        product_name = request.POST['product_name']
        products = price_comp(product_name)
        # return JsonResponse(context)
        return render(request, 'compare/result.html', {"product_name": product_name, "products": products})
