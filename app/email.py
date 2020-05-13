from flask_mail import Message
from flask import render_template,current_app
from . import mail

sender_email = 'derrickip34@gmail.com'

def send_welcome_email(to,**kwargs):
    msg = Message('Welcome',sender=sender_email,recipients=[to])
    msg.body = render_template('email/welcome_user.txt')
    msg.html = render_template('email/welcome_user.html')
    mail.send(msg)

def send_daily_email(to,**kwargs):
    email = Message('Music store daily recomendations',sender=sender_email,recipients=[to])
    email.html = render_template('email/new_blog.html')
