# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    todo = StringField("Enter your todo", validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField("Submit")


class TodoListForm(FlaskForm):
    title = StringField(
        "Enter your todolist title", validators=[DataRequired(), Length(1, 128)]
    )
    submit = SubmitField("Submit")
