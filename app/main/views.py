# from flask import render_template,redirect,url_for, abort,request,flash
from flask import render_template,redirect,url_for, abort

from . import main

from .forms import UpdateProfile
from ..models import User
from flask_login import login_required, current_user
from .. import db, photos
import markdown2
from ..email import mail_message


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome this is where you belong'

    
    

    return render_template('index.html', title = title)


@main.route('/home')
def about():
    '''
    View root page function that returns the home page and its data
    '''
    title = 'Welcome to music store'
    return render_template('home.html', title=title)

@main.route('/about')
def about():
    '''
    View root page function that returns the about page and its data
    '''
    title = ''
    return render_template('about.html', title=title)

@main.route('/contact')
def contact():
    '''
    View root page function that returns the contact page and its data
    '''
    title = ''
    return render_template('contacts.html', title = title)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)




