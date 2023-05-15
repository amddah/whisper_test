from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField

class Myform(FlaskForm):
    name=StringField(label='username')
    Password = PasswordField(label='pass')
