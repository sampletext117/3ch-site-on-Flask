from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask import request


class AddPostForm(FlaskForm):
    title = TextAreaField('Тема вашего поста', validators=[DataRequired()])
    content = TextAreaField('Текст поста', validators=[DataRequired()])
    submit = SubmitField('Добавить')
