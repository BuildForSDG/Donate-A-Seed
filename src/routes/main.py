from flask import Blueprint, render_template
from flask_login import login_required, current_user

from src.extensions import db
from src.models import Donated
from src.models import User


main = Blueprint('main', __name__)

donate = Blueprint('donate', __name__)

#home
@main.route('/')
@main.route('/index.html')
def index():
    return render_template('index.html')

#donate
@main.route('/donate')
@main.route('/donate.html')
def donate():
    
    return render_template('donate.html')

#shop
@main.route('/shop')
@main.route('/shop.html')
def shop():
    return render_template('shop.html')

#users
@main.route('/users')
@main.route('/users.html')
@login_required
def users():
    username = current_user.username
    users = User.query.all()

    context = {
        'users' : users
    }
    
    return render_template('users.html', **context,  username=current_user.username)