from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import AccountModel
from .models import RecordModel
from .models import UserPassportModel
import json
from datetime import date
import time
import datetime
import random
from django.core import serializers
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.core.files.storage import default_storage
from deepface import DeepFace


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
        accountModel.lastname = form['lastname'].capitalize()
        accountModel.firstname = form['firstname'].capitalize()
        accountModel.othername = form['othername'].capitalize()
        accountModel.email_one = form['email_one'].lower()
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
            feedback = {
                'title': 'Successful',
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'New record has been successfully created, now redirecting...',
                'redirect': 'users',
                'info': '',
            }
            return JsonResponse(feedback, safe=False)
        else:
            feedback = {
                'title': 'Invalid',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'The request could not be processed. This may be that the recor already exist, kindly confirm the details before you continue.',
                'redirect': '',
                'info': '',
            }
        return JsonResponse(feedback, safe=False)

    except Exception as e:
        if 'Duplicate' in str(e):
            feedback = {
                'title': 'error',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'The email, personal ID, or phone number provided already in use, please confirm or try again with another.',
                'redirect': '',
                'info': '',
                'error': str(e),
        }
        else:
            feedback = {
                    'title': 'error',
                    'status': 'failed',
                    'statusmsg': '',
                    'msg': 'Something went wrong, please try again or report this error.',
                    'redirect': '',
                    'info': '',
                    'error': str(e),
            }
        return JsonResponse(feedback, safe=False)


def userUploadPassport(request):
    feedback = ''
    todayDate = date.today()
    timeNow = time.strftime("%H:%M:%S", time.localtime())
    split_id = str(todayDate).replace('-', '') +''+ str(timeNow).replace(':', '')
    split_id_List = list(split_id)
    random.shuffle(split_id_List)
    generated_id = ''.join(split_id_List)
    location = 'passports/'
    frame_counter = 0
    generateId = str(int(round(time.time() * 1000)))
    fileblob = request.FILES['filename']
    splitName = fileblob.name.split('.')
    ext = splitName[1]
    file_name = generateId+'.'+ext
    default_storage.save(location+file_name, fileblob)
    url = default_storage.url(location+file_name)
    userPassportModel = UserPassportModel()
    file_size = '300'
    file_width = '300'
    file_height = '300'
    try:
        userPassportModel.id = 0
        userPassportModel.userid = request.POST['id']
        userPassportModel.file_name = file_name
        userPassportModel.file_size = file_size
        userPassportModel.file_width = file_width
        userPassportModel.file_height = file_height
        userPassportModel.file_ext = ext
        userPassportModel.file_url = url
        userPassportModel.file_title = ''
        userPassportModel.date_created = date.today()
        userPassportModel.time_created = datetime.datetime.now()
        userPassportModel.generated_id = generated_id
        if request.method == 'POST':
            a = userPassportModel.save()

            feedback = {
                'title': 'Successful',
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'New passport has been successfully uploaded, now redirecting...',
                'redirect': '../../users',
                'info': '',
            }
            return JsonResponse(feedback, safe=False)
        else:
            feedback = {
                'title': 'Invalid',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'The request could not be processed. This may be that the record already exist, kindly confirm the details before you continue.',
                'redirect': '',
                'info': '',
            }
        return JsonResponse(feedback, safe=False)

    except Exception as e:
        if 'Duplicate' in str(e):
            feedback = {
                'title': 'error',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'This user passport already exist, please confirm or try again.',
                'redirect': '',
                'info': '',
                'error': str(e),
        }
        else:
            feedback = {
                    'title': 'error',
                    'status': 'failed',
                    'statusmsg': '',
                    'msg': 'Something went wrong, please try again or report this error.',
                    'redirect': '',
                    'info': '',
                    'error': str(e),
            }
        return JsonResponse(feedback, safe=False)


def records(request):
    feedback = ''
    try:
        if request.method == 'GET':
            data = RecordModel.objects.values().order_by('-id')
            if len(data) > 0:
                feedback = {
                    'title': 'Successful',
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'redirect': '',
                    'info': list(data),
                }
                return JsonResponse(feedback, safe=False)
            else:
                feedback = {
                    'title': 'norecord',
                    'status': 'failed',
                    'statusmsg': '',
                    'msg': 'No record(s) found',
                    'redirect': '',
                    'info': '',
                }
                return JsonResponse(feedback, safe=False)
        else:
            feedback = {
                'title': 'error',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'Something went wrong, please try again or report this error.',
                'redirect': '',
                'info': '',
                'error': str(e),
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
        return JsonResponse(feedback, safe=False)


def userData(id):
    feedback = ''
    try:
        data = RecordModel.objects.filter(generated_id=id).values('id', 'lastname', 'firstname', 'email_one')
        if len(data) > 0:
            feedback = {
                'status': True,
                'data': data[0],
            }
            return feedback
        else:
            feedback = {
                'status': False,
                'data': '',
            }
            return feedback

    except Exception as e:
        return 'error '+ str(e)

def userInfo(id):
    feedback = ''
    try:
        data = RecordModel.objects.filter(email_one=id).values('id', 'file_url', 'lastname', 'firstname', 'email_one')
        if len(data) > 0:
            feedback = {
                'status': True,
                'data': data[0],
            }
            return feedback
        else:
            feedback = {
                'status': False,
                'data': '',
            }
            return feedback

    except Exception as e:
        return 'error '+ str(e)



def compareFace(request):
    feedback = ''
    todayDate = date.today()
    timeNow = time.strftime("%H:%M:%S", time.localtime())
    split_id = str(todayDate).replace('-', '') +''+ str(timeNow).replace(':', '')
    split_id_List = list(split_id)
    random.shuffle(split_id_List)
    generated_id = ''.join(split_id_List)
    location = 'temporary/'
    frame_counter = 0
    generateId = str(int(round(time.time() * 1000)))
    fileblob = request.FILES['filename']
    splitName = fileblob.name.split('.')
    ext = splitName[1]
    file_name = generateId+'.'+ext
    default_storage.save(location+file_name, fileblob)
    url = default_storage.url(location+file_name)
    incomingImage = url
    userId = request.POST['userid']
    getData = userInfo(userId)
    getUserPassportUrl = getData['data']['file_url']
    getUserPassportUrl = getUserPassportUrl[1:]
    incomingImage = incomingImage[1:]
    try:
        compare = DeepFace.verify(getUserPassportUrl, incomingImage)
        if compare:
            feedback = {
                'title': 'Successful',
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'Face matched successfully, now redirecting...',
                'redirect': 'dashboard/'+str(getData['data']['lastname']),
                'info': '',
            }
            return JsonResponse(feedback, safe=False)
        else:
            feedback = {
                'title': 'Invalid',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'Error recongnizing your face, please try again.',
                'redirect': '',
                'info': '',
            }
        return JsonResponse(feedback, safe=False)

    except Exception as e:
        feedback = {
                'title': 'error',
                'status': 'failed',
                'statusmsg': '',
                'msg': 'Something went wrong or the face do not match, kindly ensure the face is well captured, please try again.',
                'redirect': '',
                'info': '',
                'error': str(e),
        }
        return JsonResponse(feedback, safe=False)