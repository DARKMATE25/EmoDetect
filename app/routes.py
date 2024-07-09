# app/routes.py

from flask import render_template, request, jsonify
from app import app, mail
from flask_mail import Message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    # Get input values for each emotion
    # ...

    # Perform depression calculation
    # ...

    # Construct the depression report
    depression_report = f"Depression Percentage: {depression_percentage:.2f}%"

    # Send email
    recipient_email = request.form.get('recipientEmail')
    send_email('Depression Report', depression_report, recipient_email)

    return render_template('index.html', result=depression_report)

def send_email(subject, body, recipient_email):
    msg = Message(subject, recipients=[recipient_email])
    msg.body = body

    try:
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
