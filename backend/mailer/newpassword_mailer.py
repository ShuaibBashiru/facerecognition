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

current_file = 'Password mailer'


def new_password_mailer(email, username, code):
    # welcome = 'You are welcome,'
    mailername = 'Yabatech Prestige Cooperative'
    sitename = 'Yabatech Prestige Cooperative Portal'
    slogan = 'Doing Business With Human Face'
    sender_email = "yctprestigeinfo@gmail.com"
    yagmail.register(sender_email, 'General321.')
    subject = "Yabatech Prestige Account Password"
    link = 'https://www.yabatechprestige.org'
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

        receiver_email = email
        mailername = mailername
        slogan = slogan

        html = """\
          <h2 style="margin: 0px;">Hello, {}</h2>
          <p style="margin: 0px;">Kindly use the code below to generate a new password.</p>
            <h1>{}</h1>
            <p style="margin: 0px; padding:0px;">You are receiving this because you either just created an account or you 
                requested for a new password,\nif you did not make any request, you can safely ignore this email.</p>
            <p style="margin: 0px; padding:0px;">
            Thank You!
            {}\n{}\n{}
            </p>
        """.format(username, code, mailername, link, slogan)

        yag = yagmail.SMTP(sender_email)

        yag.send(
            # from = receiver_email,
            to=receiver_email,
            subject=subject,
            contents=html,
        )
        return True
    except Exception as e:
        write_error(current_file, e)
        return False


def admin_password(email, username, code):
    # welcome = 'You are welcome,'
    mailername = 'Yabatech Prestige Cooperative'
    sitename = 'Yabatech Prestige Cooperative Portal'
    slogan = 'Doing Business With Human Face'
    sender_email = "yctprestigeinfo@gmail.com"
    yagmail.register(sender_email, 'General321.')
    subject = "Yabatech Prestige Account Password"
    link = 'https://www.yabatechprestige.org'
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

        receiver_email = email
        mailername = mailername
        slogan = slogan

        html = """\
        <h2 style="margin: 0px;">Hello, {}</h2>
          <p style="margin: 0px;">Kindly use the code below to generate a new password.</p>
            <h1>{}</h1>
            <p style="margin: 0px; padding:0px;">You are receiving this email because you are just been given access to 
            manage the {}, if you have any enquiry regarding this notification, 
            kindly contact the Administrator.</p>
            <p style="margin: 0px; padding:0px;">
            Thank You!
            {}\n{}\n{}
            </p>
        """.format(username, code, sitename, mailername, link, slogan)

        yag = yagmail.SMTP(sender_email)

        yag.send(
            # from = receiver_email,
            to=receiver_email,
            subject=subject,
            contents=html,
        )
        return True
    except Exception as e:
        write_error(current_file, e)
        return False


def mailer_change(email, username):
    # welcome = 'You are welcome,'
    mailername = 'Yabatech Prestige Cooperative'
    sitename = 'Yabatech Prestige Cooperative Portal'
    slogan = 'Doing Business With Human Face'
    sender_email = "yctprestigeinfo@gmail.com"
    yagmail.register(sender_email, 'General321.')
    subject = "Yabatech Prestige Account Password"
    link = 'https://www.yabatechprestige.org'
    try:
        receiver_email = email
        mailername = mailername
        slogan = slogan

        html = """\
        <h2 style="margin: 0px;">{}</h2>
            <p style="margin: 0px; padding:0px;">You are receiving this email because you either 
            request for new password or you just changed password. 
            If you did not initiate this, kindly contact the administrator', 
            <p style="margin: 0px; padding:0px;">
            Thank You!
            {}\n{}\n{}
            </p>
        """.format(username, mailername, link, slogan)

        yag = yagmail.SMTP(sender_email)

        yag.send(
            # from = receiver_email,
            to=receiver_email,
            subject=subject,
            contents=html,
        )
        return True
    except Exception as e:
        write_error(current_file, e)
        return False
