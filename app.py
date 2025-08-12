#!/usr/bin/python3
import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect
from form_contact import ContactForm
from api.messages_api import messages_api

# Initialize app
app = Flask(__name__)

# CSRF and Secret Key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)

# Register API Blueprint
app.register_blueprint(messages_api)
csrf.exempt(messages_api)  # Allow Postman to work without CSRF token

# Email config (replace with your actual credentials)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourPassword'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Routes
@app.route('/')
def index():
    return render_template('views/home/index.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])
        print('-------------------------')
        send_message(request.form)
        return redirect('/success')

    return render_template('views/contacts/contact.html', form=form)

@app.route('/success')
def success():
    return render_template('views/home/index.html')

def send_message(message):
    print(message.get('name'))
    msg = Message(
        message.get('subject'),
        sender=message.get('email'),
        recipients=['id1@gmail.com'],
        body=message.get('message')
    )
    mail.send(msg)

# Optional: HTML page to show API messages
@app.route('/messages')
def view_messages():
    return render_template('messages.html')

# Run server
if __name__ == "__main__":
    app.run(debug=True)
