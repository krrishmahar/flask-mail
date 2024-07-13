from flask import Blueprint, jsonify
from smtplib import SMTPException
from flask_mail import Message
from app import app, mail

bp = Blueprint('routes', __name__)

@app.route('/')
def publish():
    try:
        with mail.connect() as conn:
            msg = Message(
                '[mail app demo] Test case',
                sender=app.config["MAIL_SENDER"],
                recipients=['test-fi3ylmc1j@srv1.mail-tester.com'],
                body="This is the plain text version of the email. It is important to have a plain text version for better deliverability.",
                html="""
                <html>
                    <body>
                        This is the <b>HTML</b> body.<br>
                        <p>Thank you for using our service!</p>
                    </body>
                </html>
                """
            )
            conn.send(msg)
        return jsonify({'message': 'Your message has been sent successfully'}), 200
    except SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return jsonify({'message': 'Failed to send email due to SMTP error'}), 500
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'message': 'Failed to send email due to an unexpected error'}), 500
