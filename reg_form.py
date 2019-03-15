from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Ваш логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    birth_date = StringField('Ваша дата рождения', validators=[DataRequired()])
    submit = SubmitField('Войти')