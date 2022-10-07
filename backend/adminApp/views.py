from django.shortcuts import render, redirect, HttpResponse

from . import userView

# Create your views here.
def signin(request):
    data = {'name': 'home'}
    return render(request, "admin/signin.html", data)

def dashboard(request):
    data = {'name': 'home'}
    return render(request, "admin/dashboard.html", data)

def users(request):
    data = {'name': 'Enrol'}
    return render(request, "admin/users.html", data)

def newEnrol(request, id):
    record = userView.userData(id)
    data = {'data': record['data']}
    if record['status'] == True:
        return render(request, "admin/enrolment.html", data)
    else:
        return redirect('/admin/users')

def createUser(request):
    data = {'name': 'Create account'}
    return render(request, "admin/createAccount.html", data)