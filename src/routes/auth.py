from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from src.extensions import db
from src.models import User

auth = Blueprint('auth', __name__)


@auth.route('/registerfarmer.html', methods=['GET', 'POST'])
def registerfarmer():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        state = request.form['state']
        lga = request.form['lga']
        phone = request.form['phone']
        bvn = request.form['bvn']

        unhashed_password = request.form['password']

        user = User(lastname=lastname,
                    firstname=firstname,
                    username=username,
                    email=email,
                    address=address,
                    state=state,
                    lga=lga,
                    phone=phone,
                    bvn=bvn,
                    unhashed_password=unhashed_password,
                    farmer=True,
                    seeder=False,
                    admin=False)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('registerfarmer.html')


@auth.route('/registerseed.html', methods=['GET', 'POST'])
def registerseed():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        state = request.form['state']
        lga = request.form['lga']
        phone = request.form['phone']
        bvn = request.form['bvn']

        unhashed_password = request.form['password']

        user = User(lastname=lastname,
                    firstname=firstname,
                    username=username,
                    email=email,
                    address=address,
                    state=state,
                    lga=lga,
                    phone=phone,
                    bvn=bvn,
                    unhashed_password=unhashed_password,
                    farmer=False,
                    seeder=True,
                    admin=False)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('registerseed.html')


@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            error_message = str("pls check details")
            print(error_message)

        else:
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
