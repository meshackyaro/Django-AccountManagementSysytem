from django.shortcuts import render, HttpResponse

# Create your views here.


# def say_hello(request):
#     return HttpResponse("Hello, welcome to django-account-management-system!")

# def welcome(request, name):
#     return HttpResponse(f"Hello, {name} welcome to django-account-management-system!")

def welcome(request, name):
    return render(request, 'index.html', {'name': name})
