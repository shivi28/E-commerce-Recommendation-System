from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
# Commented out to avoid celery dependency for now
# from cashback.celery_tasks import app
#from cashback.user_login.models import *
#from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from user_login.models import Customer



@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

def SignupTask(email):
    subject = 'Welcome to Cashback'
    from_email = 'madhurmadhur@docarto.com'
    to_email_list = [email]
    html_message = '<h1>Welcome to Cashback</h1>'
    email_message = EmailMultiAlternatives(subject, html_message, from_email, to_email_list)
    email_message.attach_alternative(html_message, 'text/html')
    email_message.send()

def SendOfferEmail(html_message, category):
    subject = 'Offers from '+category.name
    from_email = 'madhurmadhur@docarto.com'
    to_email_list = ['madhur@vassarlabs.com']
    email_message = EmailMultiAlternatives(subject, html_message, from_email, to_email_list)
    email_message.attach_alternative(html_message, 'text/html')
    email_message.send()
