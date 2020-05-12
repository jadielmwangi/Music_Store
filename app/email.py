from flask_mail import Message
from flask import render_template,current_app
from . import mail
from celery import Celery

client = Celery(current_app.name, broker=current_app.config['CELERY_BROKER_URL'])
client.conf.update(current_app.config)

sender_email = current_app.config['MAIL_USERNAME']

def send_welcome_email(to):
    msg = Message('Welcome',sender=sender_email,recipients=[to])
    msg.body = render_template('email/welcome_user.txt')
    msg.html = render_template('email/welcome_user.html')
    mail.send(msg)

@client.task
def send_daily_email(**kwargs):
    email = Message('Music store daily recomendations',sender=sender_email,recipients=[to])
    email.html = render_template('email/new_blog.html')

    if duration_unit == 'minutes':
        duration *= 60
    elif duration_unit == 'hours':
        duration *= 3600
    elif duration_unit == 'days':
        duration *= 86400