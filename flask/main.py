from flask import Flask
from flask import send_file
import getpass
from datetime import datetime
from datetime import timedelta
import socket

app = Flask(__name__)

heartbeat_file_abspath = "/home/" + getpass.getuser() + "/heartbeat.txt"
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
def style():
    return """
    <style>
        table, th, td {
          border:1px solid black;
        }
    </style>
    """
def enclose(input, tag):
    return "<" + tag + ">" + input + "</" + tag + ">"

def tr(input):
    return "<tr>" + input + "</tr>"
def th(input):
    return "<th>" + input + "</th>"

def downtime_table():
    values = []
    table = "<table><thead><th>downtime start</th><th>downtime end</th><th>duration (approx minutes)</th></thead>"
    with open(heartbeat_file_abspath) as f_ping:
        lines = f_ping.readlines()
        for line in lines:
            values.append(int("".join(c for c in line if c.isdigit())))

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

def heading_text():
    return "<h1>Downtimes</h1>"

def download_ping():
    return "<a href=http://" + IPAddr + ":8080/heartbeatfile download>download hearbeat file</a>"
@app.route('/')
def hello():
    prolog = enclose(heading_text(), "div")
    table = enclose(downtime_table(), "div")
    download = enclose(download_ping(), "div")
    return enclose(style() + enclose(prolog + table + download, "body"), "html")

@app.route('/heartbeatfile')
def return_hearbeat_file():
    try:
        return send_file(heartbeat_file_abspath)
    except Exception as e:
        return str(e)

app.run(host='0.0.0.0', port=8080)