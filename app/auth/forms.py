from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import input_required,Email,EqualTo
from ..models import *
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField



class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[input_required(),Email()])
    username = StringField('Enter your username',validators = [input_required()])
    password = PasswordField('Password',validators = [input_required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [input_required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')


    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[input_required(),Email()])
    password = PasswordField('Password',validators =[input_required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')