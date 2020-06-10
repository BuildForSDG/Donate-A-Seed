from flask import Blueprint, render_template, request, jsonify, json, redirect, flash, url_for
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
@main.route('/donate.html', methods=['POST','GET'])
def donate():

    return render_template('donate.html')

#donated
@main.route('/donated', methods=['POST' , 'GET'])
def donated():
    if request.method == 'POST':
        donate_amount = request.form['donate-amount']
        donated_by_email = request.form['donator-email']
        donator_name = request.form['donator-name']

        #new_donator = Donated (
        #    donate_amount=donate_amount,
        #    donated_by_email=donated_by_email,
        #    donator_name=donator_name
        #)
                                
        #db.session.add(new_donator)
        #db.session.commit()

        return jsonify({'Thanks' : "Thank you" + donator_name + "for your Donation of" + donate_amount})

        #flash('Thank you {} for your Donations. It means a lot to us'.format(donator_name), 'success')

        #return redirect(url_for('main.index'))

    return render_template('donated.html')


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