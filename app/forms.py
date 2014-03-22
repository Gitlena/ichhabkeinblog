__author__ = 'PeMac'


from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    passwrd = 