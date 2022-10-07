import cv2
from django.http import JsonResponse
from django.http import HttpResponse
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
import mimetypes
import base64
import imutils
import threading
#import matplotlib.pyplot as plt
#import face_recognition



current_file = "Login"


def authenticate(request):
    feedback = ''
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
                counter = cursor.execute("SELECT id, surname, firstname, othername, email_one, phone_one, "
                                         "applicant_number FROM user_record WHERE email_one=%s AND surname=%s LIMIT "
                                         "1", [userid, pwd])
                row = dictfetchall(cursor)
                if counter > 0:
                    newuserid = row[0]['id']

                    res = startCamera(request, newuserid)
                    if res == 1:
                        request.session['userdata'] = row[0]
                        request.session['activeid'] = activeid
                        request.session['sessionHash'] = activeid + str(row[0]['email_one']).lower()
                        userdata = {
                            'id': request.session['userdata']['id'],
                            'surname': request.session['userdata']['surname'],
                            'firstname': request.session['userdata']['firstname'],
                            'othername': request.session['userdata']['othername'],
                            'email_one': request.session['userdata']['email_one'],
                            'phone_one': request.session['userdata']['phone_one'],
                            'applicant_number': request.session['userdata']['applicant_number'],
                        }

                        feedback = {
                            'status': 'success',
                            'statusmsg': 'success',
                            'msg': 'Authentication successful, redirecting..',
                            'result': userdata,
                            'redirect': '/secure/dashboard/?info=' + str(row[0]['email_one']).lower() + 'id=' + activeid,
                            'classname': 'alert-primary p-2',
                        }

                    elif res == 2:
                        feedback = {
                            'status': 'failed',
                            'statusmsg': 'error',
                            'msg': 'You have not enrolled on this platform',
                            'result': 'userdata',
                            'classname': 'alert-danger p-2',
                        }

                    elif res == 3:
                        feedback = {
                            'status': 'failed',
                            'statusmsg': 'error',
                            'msg': 'Your face do not match the details provided, if this account belongs to you, '
                                   'please use a brighter environment for authentication ',
                            'result': 'userdata',
                            'classname': 'alert-danger p-2',
                        }
                    else:
                        feedback = {
                            'status': 'failed',
                            'statusmsg': 'error',
                            'msg': 'Something went wrong or you have not enrolled your face! Please use a brighter '
                                   'environment and try again',
                            'result': '',
                            'redirect': '/site/signin',
                            'classname': 'alert-danger p-2',
                        }

                else:
                    feedback = {
                        'status': 'failed',
                        'statusmsg': 'error',
                        'msg': 'Incorrect username and/or password.',
                        'result': '',
                        'redirect': '/site/signin',
                        'classname': 'alert-danger p-2',
                    }

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
        return JsonResponse(feedback, safe=False)


def startCamera(request, newuserid):
    # data = np.zeros((1140, 2560))
    # image = plt.savefig(data)
    success = 0
    failed = 0
    notexist = 0
    image_base64 = ''
    location = 'static/tmp_uploaded/'
    passportLoc = 'static/passport/'
    frame_counter = 0
    filename = str(int(round(time.time() * 1000)))
    new_filename = ''

    h = 200
    w = 200
    y = 0
    x = 0
    try:
        cam = cv2.VideoCapture(0)
        result = True
        while result:
            ret, frame = cam.read()
            frame = imutils.resize(frame, width=w, height=h)
            if not ret:
                break
            cv2.imshow("Passport", frame)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                break
            elif k % 256 == 32:
                img_name = "{}.png".format(filename)
                new_filename = img_name
                cv2.imwrite(location + img_name, frame)
                image = cv2.imread(location + img_name)
                crop_image = image[x:w, y:h]
                cv2.imwrite(location + img_name, crop_image)
                result = False
        cam.release()
        cv2.destroyAllWindows()

        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT id, passport_name FROM passport_tbl WHERE user_id =%s",
                                     [newuserid, ])
            row = dictfetchall(cursor)

            if counter > 0:
                cursor.close()
                old_filename = row[0]['passport_name']
                known_image = face_recognition.load_image_file(passportLoc + old_filename)
                unknown_image = face_recognition.load_image_file(location + new_filename)
                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
                result = face_recognition.compare_faces(
                    [known_image_encoding], unknown_image_encoding, tolerance=0.40)
                # check if it was a match
                if result[0]:
                    return 1
                else:
                    return 3
            else:
                return 2

    except Exception as e:
        write_error(current_file, e)
        return 4
