from flask import Blueprint, render_template, request, redirect, url_for, Flask, flash, Markup
from flask_login import login_user, logout_user
#from flask_admin import Admin
from werkzeug.security import check_password_hash
from flask_mail import Mail
from src.extensions import db
from src.models import User
import smtplib
from email.message import EmailMessage
from wtforms.validators import InputRequired

auth = Blueprint('auth', __name__)


#function for register
@auth.route('/register.html', methods=['GET', 'POST'])
def register():
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
        usertype = request.form['usertype']

        
#check if username exists
        checkusername = User.query.filter_by(username=username).first()

        if checkusername:
            flash(' Username already exists', 'error')
            return redirect(url_for('auth.login'))

#check if email already exists
        checkuseremail = User.query.filter_by(email=email).first()

        if checkuseremail:
            flash(' Email Address already exists', 'error')
            return redirect(url_for('auth.login'))


        new_user = User(lastname=lastname,
                    firstname=firstname,
                    username=username,
                    unhashed_password=unhashed_password,
                    email=email,
                    address=address,
                    state=state,
                    lga=lga,
                    phone=phone,
                    bvn=bvn,
                    usertype=usertype
                    )
                    
        db.session.add(new_user)
        db.session.commit()

        #email message
        msg = EmailMessage()
        msg['Subject'] = 'Donate A Seed - Confirmation Email'
        msg['From'] = "donateaseedoffcial@gmail.com"
        msg['To'] = email
        msg.set_content('')
        msg.add_alternative("""\
        <h1 style="color: #000; font-weight: 600; text-align: center;">Confirmation Email for your Application On Donate A Seed</h1>
        <br>
        <p style="color: #222; font-weight: 300;">Hi {}, Your email {} was used for applying on <b>Donate A Seed</b> as a <b>{}</b>.
        <br>
        We will review your application and send your results to {} <br>
        Please ignore this email if you did not apply on our platform. </p>

        <br>For any enquiries reply to this email and we will get back to you as soon as possible.
        <br><br><br>
        Regards,<br>
        Donate A Seed
        """.format(firstname,email,usertype,email), subtype='html')

        #email sending function
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("donateaseedoffcial@gmail.com", "donateaseed1234")
            smtp.send_message(msg)

        flash(' Registered successfully, please check your email.', 'success')

        return redirect(url_for('auth.login'))

    return render_template('register.html')



#function for login
@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False

#validate details
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash(' Could not Login, Please check your login details and try again', 'error')

        else:
            login_user(user, remember=remember)
            return redirect(url_for('main.users'))

    return render_template('login.html')


@auth.route('/logout.html')
def logout():
    logout_user()
    flash('Logged Out successfully', 'success')
    return redirect(url_for('auth.login'))
