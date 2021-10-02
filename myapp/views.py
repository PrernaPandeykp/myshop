from django.shortcuts import render,HttpResponse
from .models import Product as Product_view 
from .models import Publisher
from math import ceil
import csv
# Create your views here.


'''
def main(request):
    allprods=[]
    cat_prods=Product.objects.values('category','id')
    cats={item['category'] for item in cat_prods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4 + ceil((n/4) -(n//4))
        allprods.append([prod,range(1,nslides),nslides])
    
    params= {'allprods':allprods}
    return render(request,"main.html",params)
'''
def about(request):
    return render(request,"about.html")
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        print(username,password)
    return render(request,"login.html")


def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productview(request):
    return HttpResponse("product")

def checkout(request):
    return HttpResponse("checkout")

def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'IP Address'])

    for member in Product_view.objects.all().values_list('first_name', 'last_name', 'email', 'ip_address'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    return response
