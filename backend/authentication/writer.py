from django.http import JsonResponse
import os
import time
import json
import sys
#import serial
import random
import datetime


def write_error(name, e):
    feedback = ''
    file = './logs/error_log.txt'
    try:
        reader = open(file, 'a')
        message = '{From: ' + str(name)+', Date: ' + str(datetime.datetime.now()) \
                  + ', Error found: ' + str(e) + '}__error_log__'
        reader.write(f'\n{message}')
    except KeyError as e:
        feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! Technical issue, kindly contact'
                       ' our support desk to report this case. Thanks',
                'classname': 'alert-danger p-2',
            }
    return JsonResponse(feedback, safe=False)


def write_activity(name, e):
    feedback = ''
    file = './logs/activity_log.txt'
    try:
        reader = open(file, 'a')
        message = '{From: ' + str(name)+', Date: ' + str(datetime.datetime.now()) \
                  + ', Activity: ' + str(e) + '}__error_log__'
        reader.write(f'\n{message}')
    except KeyError as e:
        feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! Technical issue, kindly contact'
                       ' our support desk to report this case. Thanks',
                'classname': 'alert-danger p-2',
            }
    return JsonResponse(feedback, safe=False)
