from django.shortcuts import render, HttpResponse

def index(request):
    data = {'name': 'Home page'}
    return render(request, "app/home.html", data)

def logout(request):
    data = {'name': 'Logout'}
    return render(request, "app/home.html", data)