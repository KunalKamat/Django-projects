from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def food(request):
    return render(request,'food.html')

def contact(request):
    return render(request,'contact.html')

def Historical(request):
    return render(request,'Historical.html')

def Entertainment(request):
    return render(request,'Entertainment.html')

def Shopping (request):
     return render(request,'Shopping.html')

def about(request):
    return render(request,'about.html')

