from flask_wtf import Form
from wtforms import BooleanField, SubmitField

class UpdateForm(Form):
   id = BooleanField('Interesting?')
   submit = SubmitField('Update')