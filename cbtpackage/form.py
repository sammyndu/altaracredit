from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SubmitField, RadioField, DateField, IntegerField, FileField, SelectField
from wtforms.validators import DataRequired, Email

class AddBooks(FlaskForm):
    book_title = StringField("Book Title: ", validators=[DataRequired()])
    book_description = TextAreaField("Book Description: ", validators=[DataRequired()])
    book_author = StringField("Book Author: ", validators=[DataRequired()])
    status = SelectField(choices=[('Available','Available'),('Unavailable','Unavailable')])
    submit = SubmitField("Add Book")