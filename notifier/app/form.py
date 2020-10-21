from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class SubscribeForm(FlaskForm):
    full_name = StringField('Your Name', [
        DataRequired(message='Your name is required'),
        Length(min=3, message='Please enter your name')
    ])
    email_address = EmailField('Your Email', [
        DataRequired(message='Email is required'),
        Length(min=10, message='Please enter valid email address')
    ])
    submit = SubmitField('Notify me!')


class ContactForm(FlaskForm):
    full_name = StringField('Your Name', [
        DataRequired(message='Your name is required'),
        Length(min=3, message='Please enter your name')
    ])
    email_address = EmailField('Your Email', [
        DataRequired(message='Email is required'),
        Length(min=10, message='Please enter valid email address')
    ])
    subject = StringField('Your Name', [
        DataRequired(message='Please enter subject'),
        Length(min=8, message='Please enter at least 8 chars of subject')
    ])
    message = StringField('Your Name', [
        DataRequired(message='Please write something for us'),
        Length(min=5, message='Please write something for us')
    ])
    submit = SubmitField('Send Message')