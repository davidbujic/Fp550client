from flask_wtf import Form
from wtforms import SubmitField, RadioField, TextField, IntegerField

class CommandsForm(Form):
    Commands = RadioField('Commands', choices = [('G11','G1.1 DateTime'),('G12','G1.2 PIB'),('G13','G1.3 Move paper'),('G14','G1.4 Status'),('G15','G1.5 Tax'),('G16','G1.6 Diag'),('G17','G1.7 All Articles'),('G18','G1.8 Set Taxes')])
    Data = TextField('Data')
    Subdomain = TextField('Subdomain')
    submit = SubmitField("Send Request")
class CustomCommandForm(Form):
    Command = IntegerField('Command')
    Data = TextField('Data')
    submit = SubmitField('Send')
class G31Form(Form):
    Data = TextField('Data')
    Subdomain = TextField('Subdomain')
    submit = SubmitField('Send')
