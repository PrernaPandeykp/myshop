from django.shortcuts import render,HttpResponse
# Create your views here.

def main(request):
    return render(request,'blog/index.html')
