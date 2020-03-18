from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from rsppost.models import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('邮箱',
                        validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('这个名字已经被使用了，请换一个吧！')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('这个邮箱已经被使用了，请换一个吧！')


class LoginForm(FlaskForm):
    email = StringField('邮箱',
                        validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('保持登录状态')
    submit = SubmitField('Login')

class Login_with_username_Form(FlaskForm):
    username = StringField('用户名',
                        validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('保持登录状态')
    submit = SubmitField('Login')