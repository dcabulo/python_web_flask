from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField


class LoginForm(Form):
    user_name = StringField('Username', [
        validators.length(min=4, max=20, message='El username se encuentra fuera de rango')
    ])
    password = PasswordField('Password', [
        validators.Required()
    ])