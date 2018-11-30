from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=5)], render_kw={"placeholder": "Name"})
    username = StringField("Username",[validators.Length(min=2)],render_kw={"placeholder": "Username"})
    password = PasswordField("Password",[validators.Length(min=6)], render_kw={"placeholder": "password"})
    passwordAgain = PasswordField("Type your password again",[validators.Length(min=6)], render_kw={"placeholder": "Type your password again"})

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=5)], render_kw={"placeholder": "Name"})
    username = StringField("Username",[validators.Length(min=2)],render_kw={"placeholder": "Name"})
