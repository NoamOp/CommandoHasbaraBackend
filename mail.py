from flask import url_for
from flask_mail import Message

from extensions import mail


# Mail
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request', sender='noreply@example.com',
        recipients=[user.email]
    )
    msg.body = f'''To reset your password, visit the following link:
    {url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no 
changes will be made.
'''
    mail.send(msg)


