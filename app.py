from flask import Flask, render_template, request, flash, redirect
from forms import CommandsForm, CustomCommandForm
import requests
import json
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/commands', methods = ['GET', 'POST'])
def commands():
    form = CommandsForm()

    if request.method == 'POST':
        Commands = request.form['Commands']
        if Commands == "G11":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=62"
        elif Commands == "G12":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=99"
        elif Commands == "G13":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=44&data="+request.form['Data']
        elif Commands == "G14":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=74"
        elif Commands == "G15":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=97"
        elif Commands == "G16":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=71"
        elif Commands == "G17":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=111&data=1"
        elif Commands == "G18":
            url = "https://fp550irvas.localtunnel.me/g1?cmd=83"
        response = requests.get(url)
        resp_dict=json.loads(response.text)
        """if type(resp_dict) is str:
            print(resp_dict)
        else:
            data_str = ""
            for m in resp_dict['recv_pck_Data']:
                data_str=data_str + chr(m)"""
        return render_template('success.html', Commands = resp_dict['recv_pck_Data'])
    elif request.method == 'GET':
        return render_template('commands.html', form = form)
@app.route('/takephoto')
def takephoto():
    url = "http://fp550irvas.localtunnel.me/g21_cmd"
    response = requests.get(url)
    resp_dict=response.text
    print resp_dict
    return redirect(resp_dict[1:-2])
@app.route('/customcommand', methods = ['GET', 'POST'])
def customcommand():
    form = CustomCommandForm()

    if request.method == 'POST':
        url = "https://fp550irvas.localtunnel.me/g1?cmd="+request.form['Command']+"&data="+request.form['Data']
        response = requests.get(url)
        resp_dict=json.loads(response.text)
        """if type(resp_dict) is str:
            print(resp_dict)
        else:
            data_str = ""
            for m in resp_dict['recv_pck_Data']:
                data_str=data_str + chr(m)"""
        return render_template('success.html', Commands = resp_dict['recv_pck_Data'])
    elif request.method == 'GET':
        return render_template('customcommand.html', form = form)
if __name__ == '__main__':
    app.run(debug = True,port=8090)