from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class ProjectForm(FlaskForm):
    name = StringField("Project name", [validators.Length(min=2)])
    time = IntegerField("Time used", [validators.NumberRange(min=0)])
    done = BooleanField("Done?")
  
    class Meta:
        csrf = False