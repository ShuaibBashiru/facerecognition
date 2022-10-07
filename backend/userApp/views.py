from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import AccountModel
import json
from datetime import date
import time
import datetime
import random

def signin(request):
    data = {'name': 'home'}
    return render(request, "user/signin.html", data)

def dashboard(request, name):
    data = {'name': name}
    print(data)
    return render(request, "user/dashboard.html", data)

def createAccount(request):
    feedback = ''
    todayDate = date.today()
    timeNow = time.strftime("%H:%M:%S", time.localtime())
    split_id = str(todayDate).replace('-', '') +''+ str(timeNow).replace(':', '')
    split_id_List = list(split_id)
    random.shuffle(split_id_List)
    generated_id = ''.join(split_id_List)
    accountModel = AccountModel()
    form = request.POST
    try:
        if form['personal_id'] !='':
            userid = form['personal_id']
        else:
            userid = generated_id

        accountModel.id = 0
        accountModel.personal_id = userid
        accountModel.lastname = form['lastname']
        accountModel.firstname = form['firstname']
        accountModel.othername = form['othername']
        accountModel.email_one = form['email_one']
        accountModel.phone_code = form['phone_code']
        accountModel.phone_one = form['phone_one']
        accountModel.gender_id = form['gender_id']
        accountModel.yob = form['yob']
        accountModel.mob = form['mob']
        accountModel.dob = form['dob']
        accountModel.date_created = date.today()
        accountModel.time_created = datetime.datetime.now()
        accountModel.generated_id = generated_id
        if request.method == 'POST':
            a = accountModel.save()
            print(str(a) + ' Returned')
            feedback = {
                'title': 'Successful',
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'New record has been successfully created, now redirecting...',
                'redirect': 'enroled',
                'info': '',
            }
            return JsonResponse(feedback, safe=False)
        else:
            feedback = {
                'title': 'Invalid',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'The record(s) could not be processed. This may be that the selected record(s) already uploaded, kindly confirm the record(s) before you continue.',
                'redirect': '',
                'info': '',
            }
        return JsonResponse(feedback, safe=False)

    except Exception as e:
        feedback = {
                'title': 'error',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'Something went wrong, please try again or report this error.',
                'redirect': '',
                'info': '',
                'error': str(e),
        }
        print(e[1])
        return JsonResponse(feedback, safe=False)


    