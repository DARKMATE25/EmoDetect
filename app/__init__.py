# app/__init__.py

from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

# Configure Flask-Mail for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ptime3304@gmail.com'
app.config['MAIL_PASSWORD'] = 'timepass0327'  # Generate an App Password in Gmail settings
app.config['MAIL_DEFAULT_SENDER'] = 'ptime3304@gmail.com'

mail = Mail(app)

from app import routes
