from flask import Flask
import getpass
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)

def style():
    return """
    <style>
        table, th, td {
          border:1px solid black;
        }
    </style>
    """
def html(input):
    return "<html>" + style() + input + "</html>"

def tr(input):
    return "<tr>" + input + "</tr>"
def th(input):
    return "<th>" + input + "</th>"
def downtime_table():
    path = "/home/" + getpass.getuser() + "/ping.txt"
    values = []
    table = "<table><thead><th>downtime start</th><th>downtime end</th><th>duration (approx minutes)</th></thead>"
    with open(path) as f_ping:
        lines = f_ping.readlines()
        for line in lines:
            values.append(int(line.replace("\n", "")))

    count = 0
    for value in values:
        if count > 0:
            offset = value - values[count - 1]
            if offset > 2:
                date_before = datetime.strptime(values[count - 1].__str__(), '%Y%m%d%H%M')
                date_after = datetime.strptime(value.__str__(), '%Y%m%d%H%M')
                delta = (date_after - date_before) / timedelta(minutes=1)
                table += tr(th(date_before.__str__()) + th(date_after.__str__()) + th(delta.__str__()))
        count+=1

    table += "</table>"
    return table

@app.route('/')
def hello():
    return html(downtime_table())

app.run(host='0.0.0.0', port=8080)