from django.shortcuts import render, HttpResponse
from .models import Product

from math import ceil
import csv

# Create your views here.


def main(request):
    allprods = []
    cat_prods = Product.objects.values("master_category")

    cats = {item["master_category"] for item in cat_prods}
    for cat in cats:
        prod = Product.objects.filter(master_category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {
        "allprods": allprods,
        "cat_prods": set(map(lambda x: x["master_category"], cat_prods)),
    }

    return render(request, "main.html", params)


def about(request):
    return render(request, "about.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
    return render(request, "login.html")


def contact(request):
    return HttpResponse("contact")


def tracker(request):
    return HttpResponse("tracker")


def search(request):
    return HttpResponse("search")


def product(request):
    return HttpResponse("product")


def checkout(request):
    return HttpResponse("checkout")
