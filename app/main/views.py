from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db,photos,music
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message
from .. import mail
from ..requests import get_quotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Think|Space'
    # Getting the quotes
    quotes = get_quotes()
    print(quotes)
    return render_template('index.html',title=title,quotes=quotes)
    

@main.route('/home')
@login_required
def home():

    title = 'Home - Think|Space'
    
    return render_template('home.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
    
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

    return render_template('profile/update.html', form=form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/user/<uname>/upload_music', methods=['POST'])
@login_required
def upload_music(uname):
    user = User.query.filter_by(username = uname).first()
    if 'music' in request.files:
        filename = music.save(request.files['music'])
        path = f'music/{filename}'
        user.music_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))



