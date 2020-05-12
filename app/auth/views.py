from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm
from flask_login import login_user,logout_user,login_required
from .. import db
from . import auth
from ..email import send_welcome_email,send_daily_email

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        send_welcome_email(user.email)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html', registration_form = form)