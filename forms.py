from flask_wtf import Form
#from wtforms import StringField, validators
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    '''username = StringField('username', [validators.DataRequired()])
    password = StringField('password', [validators.DataRequired()])'''
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
