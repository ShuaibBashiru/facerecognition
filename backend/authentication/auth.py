from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
# import pandas as pd
import os
import time
import json
import sys
#import serial
import random
import datetime
# # import numpy as np
from django.db import connection
from django.middleware import csrf
from authentication.writer import write_error
from authentication.writer import write_activity
from authentication.query_columns import dictfetchall
from django.views.decorators.csrf import csrf_exempt

current_file = "Login"

@csrf_exempt
def auth_check_session(request):
    try:
        if 'userdata' in request.session:
            write_activity(current_file, request.session['userdata']['email_one']
                           + ', pagename: ' + request.GET['pagename'])
            userdata = {
                'surname': request.session['userdata']['surname'],
                'firstname': request.session['userdata']['firstname'],
                'othername': request.session['userdata']['othername'],
                'email_one': request.session['userdata']['email_one'],
                'phone_one': request.session['userdata']['phone_one'],
            }
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'You are welcome! Please wait while we redirect you...',
                'redirect': '/secure/dashboard',
                'userdata': userdata,
                'classname': 'alert-primary p-2',
            }
        else:
            feedback = {
                'status': 'failed',
                'statusmsg': 'error',
                'msg': 'Your session has expired, now redirecting...',
                'row': '',
                'redirect': '/site/logout',
                'classname': 'alert-danger p-2',
            }
    except Exception as e:
        write_error('auth_check_session', e)
        feedback = {
            'status': 'unidentified',
            'statusmsg': 'error',
            'msg': 'Error connecting, now redirecting...',
            'row': '',
            'redirect': '/site/logout',
            'classname': 'alert-danger p-2',
        }
    return JsonResponse(feedback, safe=False)


def logout_session(request):
    if 'userdata' in request.session:
        try:
            del request.session['userdata']
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'Logging you out...',
                'row': '',
                'redirect': '/site/signin',
                'classname': 'alert-danger p-2',
            }
        except Exception as e:
            write_error('logout_session', e)
            feedback = {
                'status': 'unidentified',
                'statusmsg': 'error',
                'msg': 'Error connecting, now redirecting...',
                'row': '',
                'redirect': '/site/signin',
                'classname': 'alert-danger p-2',
            }
    else:
        feedback = {
            'status': 'inactive',
            'statusmsg': 'error',
            'msg': 'Your session has expired, now redirecting...',
            'row': '',
            'redirect': '/site/signin',
            'classname': 'alert-danger p-2',
        }
    return JsonResponse(feedback, safe=False)


def token_nizer(request):
    try:
        tokenizer = csrf.get_token(request)
        request.META['CSRF_COOKIE'] = tokenizer
        request.META['CSRF_COOKIE_USED'] = True
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': '',
            'key': '{}'.format(tokenizer),
            'classname': 'alert-danger p-2',
        }
    except Exception as e:
        write_error('token_nizer', e)
        feedback = {
            'status': 'unidentified',
            'statusmsg': 'error',
            'msg': 'Error connecting, now redirecting...',
            'row': '',
            'redirect': '/site/signin',
            'classname': 'alert-danger p-2',
        }
    return JsonResponse(feedback, safe=False)


def authenticate(request):
    if request.method != "POST":
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'result': '',
            'redirect': '/site/signin',
            'classname': 'alert-danger p-2',
        }
        return JsonResponse(feedback, safe=False)
    else:
        userid = request.POST['userid']
        pwd = request.POST['pwd']
        activeid = str(int(round(time.time() * 1000)))
        try:
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT id, surname, firstname, othername, email_one, phone_one, account_type"
                                         " FROM admin_record WHERE email_one=%s AND surname=%s LIMIT 1", [userid, pwd])
                row = dictfetchall(cursor)
                if counter > 0:
                    request.session['userdata'] = row[0]
                    request.session['activeid'] = activeid
                    request.session['sessionHash'] = activeid+str(row[0]['email_one']).lower()
                    userdata = {
                        'id': request.session['userdata']['id'],
                        'surname': request.session['userdata']['surname'],
                        'firstname': request.session['userdata']['firstname'],
                        'othername': request.session['userdata']['othername'],
                        'email_one': request.session['userdata']['email_one'],
                        'phone_one': request.session['userdata']['phone_one'],
                        'role': request.session['userdata']['account_type']
                        }
                    feedback = {
                        'status': 'success',
                        'statusmsg': 'success',
                        'msg': 'Authentication successful, redirecting..',
                        'result': userdata,
                        'redirect': '/site/auth-check/?info='+str(row[0]['email_one']).lower()+'id='+activeid,
                        'classname': 'alert-primary p-2',
                    }
                    return JsonResponse(feedback, safe=False)
                else:
                    feedback = {
                        'status': 'failed',
                        'statusmsg': 'error',
                        'msg': 'Incorrect username and/or password.',
                        'result': '',
                        'redirect': '/site/signin',
                        'classname': 'alert-danger p-2',
                    }
                    return JsonResponse(feedback, safe=False)

        except Exception as e:
            write_error('authenticate', e)
            feedback = {
                'status': 'unidentified',
                'statusmsg': 'error',
                'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
                'result': '',
                'redirect': '/site/signin',
                'classname': 'alert-danger p-2',
            }
        finally:
            cursor.close()
    return JsonResponse(feedback, safe=False)
