from flask import Blueprint, render_template, request, redirect, url_for, Flask
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from flask_mail import Mail
from src.extensions import db
from src.models import User
import smtplib
from email.message import EmailMessage

auth = Blueprint('auth', __name__)


#function for register as farmer
@auth.route('/registerfarmer.html', methods=['GET', 'POST'])
def registerfarmer():


    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        #username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        state = request.form['state']
        lga = request.form['lga']
        phone = request.form['phone']
        bvn = request.form['bvn']

        #unhashed_password = request.form['password']

        user = User(lastname=lastname,
                    firstname=firstname,
                    #username=username,
                    email=email,
                    address=address,
                    state=state,
                    lga=lga,
                    phone=phone,
                    bvn=bvn,
                    farmer=True,
                    seeder=False,
                    admin=False)

        db.session.add(user)
        db.session.commit()

        msg = EmailMessage()
        msg['Subject'] = 'Donate A Seed - Confirmation Email'
        msg['From'] = "donateaseedoffcial@gmail.com"
        msg['To'] = email
        msg.set_content('')
        msg.add_alternative("""\
        <h1 style="color: #000; font-weight: 600; text-align: center;">Confirmation Email for your Application On Donate A Seed</h1>
        <br>
        <p style="color: #222; font-weight: 300;">Hi {}, Your email {} was used for applying on <b>Donate A Seed<b> as a <b>FARMER<b>.<br>
        We will review your application and send your results to {} <br>
        Please ignore this email if you did not apply on our platform. </p>

        <br>For any enquiries reply to this email and we will get back to you as soon as possible.
        <br><br><br>
        Regards,<br>
        Donate A Seed
        """.format(firstname,email,email), subtype='html')

        #email sending function
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("donateaseedoffcial@gmail.com", "donateaseed1234")
            smtp.send_message(msg)

        return redirect(url_for('auth.registerfarmer'))

    return render_template('registerfarmer.html')



# function for register as seed deliverer
@auth.route('/registerseed.html', methods=['GET', 'POST'])
def registerseed():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
       # username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        state = request.form['state']
        lga = request.form['lga']
        phone = request.form['phone']
        bvn = request.form['bvn']

       # unhashed_password = request.form['password']

        user = User(lastname=lastname,
                    firstname=firstname,
                    #username=username,
                    email=email,
                    address=address,
                    state=state,
                    lga=lga,
                    phone=phone,
                    bvn=bvn,
                    #unhashed_password=unhashed_password,
                    farmer=False,
                    seeder=True,
                    admin=False)

        msg = EmailMessage()
        msg['Subject'] = 'Donate A Seed - Confirmation Email'
        msg['From'] = "donateaseedoffcial@gmail.com"
        msg['To'] = email
        msg.set_content('')
        msg.add_alternative("""\
        <h1 style="color: #000; font-weight: 600; text-align: center;">Confirmation Email for your Application On Donate A Seed</h1>
        <br>
        <p style="color: #222; font-weight: 300;">Hi {}, Your email {} was used for applying on <b>Donate A Seed<b> as a <b>SEED DELIVERER<b>.<br>
        We will review your application and send your results to {} <br>
        Please ignore this email if you did not apply on our platform. </p>

        <br>For any enquiries reply to this email and we will get back to you as soon as possible.
        <br><br><br>
        Regards,<br>
        Donate A Seed
        """.format(firstname,email,email), subtype='html')

        #email sending function
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("donateaseedoffcial@gmail.com", "donateaseed1234")
            smtp.send_message(msg)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.registerseed'))

    return render_template('registerseed.html')



#function for login

#@auth.route('/login.html', methods=['GET', 'POST'])
#def login():
    #if request.method == 'POST':
       # username = request.form['username']
        #password = request.form['password']

        #user = User.query.filter_by(username=username).first()

        #if not user or not check_password_hash(user.password, password):
           # error_message = str("pls check details")
           # print(error_message)

       # else:
           # login_user(user)
           # return redirect(url_for('main.index'))

   # return render_template('login.html')


#@auth.route('/logout')
#def logout():
    #logout_user()
    #return redirect(url_for('auth.login'))
