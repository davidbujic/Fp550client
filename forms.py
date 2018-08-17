from flask_wtf import Form
from wtforms import SubmitField, RadioField, TextField, IntegerField

class CommandsForm(Form):
    Commands = RadioField('Commands', choices = [('G11','G1.1 command'),('G12','G1.2 command'),('G13','G1.3 command'),('G14','G1.4 command'),('G15','G1.5 command'),('G16','G1.6 command'),('G17','G1.7 command'),('G18','G1.8 command')])
    Data = TextField('Data')
    submit = SubmitField("Send Request")
class CustomCommandForm(Form):
    Command = IntegerField('Command')
    Data = TextField('Data')
    submit = SubmitField('Send command and data')
