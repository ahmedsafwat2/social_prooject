from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        try:
            ex_user = User.query.filter_by(username=field.data).first()
            if ex_user:
                raise ValidationError("That username is taken. Please choose another.")
        except Exception as e:
        # Handle the exception or log it
            raise ValidationError("An error occurred while checking the username.")
    def validate_email(self, email):
        existing_email = User.query.filter_by(email=email.data).first()
        if existing_email:
            raise ValidationError("That email is taken. Please choose another.")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, field):
        if field.data != current_user.username:
            ex_user = User.query.filter_by(username=field.data).first()
            if ex_user:
                raise ValidationError("That username is taken. Please choose another.")
            
    def validate_email(self, email):
        if email.data != current_user.email:
            existing_email = User.query.filter_by(email=email.data).first()
            if existing_email:
                raise ValidationError("That email is taken. Please choose another.")

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit=SubmitField('Request Password Reset')

    def validate_email(self, email):
        existing_email = User.query.filter_by(email=email.data).first()
        if existing_email is None:
            raise ValidationError("There is no account with that email. you must register first")
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

