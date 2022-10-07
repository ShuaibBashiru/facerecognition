import random
import string
#import yagmail

from authentication.writer import write_error
from .models import New_password_model
import datetime
import time
import json
import sys
#import serial
import string
import random


def new_password(email, business_name, code):
    try:
        gettime = datetime.datetime.now()
        save_record = New_password_model()
        save_record.email_one = email
        save_record.resetCode = code
        save_record.status_id = 1
        save_record.expire_date = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
        save_record.date_created = str(datetime.date.today())
        save_record.time_created = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
        save_record.date_modified = str(datetime.date.today())
        save_record.time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
        save_record.save()

        sender_email = "yctprestigeinfo@gmail.com"
        yagmail.register(sender_email, 'General321.')
        receiver_email = email
        subject = "Create new Account password"
        mailername = 'The Famah Team'
        link = 'https://www.famah.com'
        resetlink = 'http://localhost:8081/site/newpassword/{}/{}'.format(email, code)
        slogan = 'To Drive Economy'

        html = """\
          <p style="margin: 0px;">Hello, {}</p>
          <p style="margin: 0px;">To create a new password use the code or click the link below: </p>
            <big>{}</big> <br/>
            {}
            <br/>
            <p style="margin: 0px; padding:0px;">You are receiving this because you either just create an account or you request for new password,\nif you did not make any request, you can safely ignore this email.</p>
            <p style="margin: 0px; padding:0px;">
            Thank You!
            {}\n{}\n{}
            </p>
        """.format(business_name, code, resetlink, mailername, link, slogan)
        yag = yagmail.SMTP(sender_email)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=html
        )
        return True
    except Exception as e:
        write_error('Forgot mailer ', e)
        return False


