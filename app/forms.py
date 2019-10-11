from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(message='The password field cannot be empty..'),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField(
        'Repeat Password',
        [validators.DataRequired(message='The confirm password field cannot be empty.')])
    accept_tos = BooleanField(
        'I accept the TOS',
        [validators.DataRequired(
            message='You have to agree to our Terms of Service.')])
    submit = SubmitField('Sign Up')

class EditProfileForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    about_me = TextAreaField('About me', [validators.Length(min=0, max=140)])
    submit = SubmitField('Submit')
