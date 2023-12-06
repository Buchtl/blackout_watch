from flask import Flask
from flask import send_file
import getpass
import json
import os.path
import network

app = Flask(__name__)

path_home = "/home/" + getpass.getuser() + "/"
heartbeat_file_abspath = path_home + "heartbeat.txt"
downtimes_file_abspath = path_home + "downtimes.json"
IPAddr = network.get_ip("192.{3}[0-9].[0-9]{1,3}.[0-9]{1,3}", 5)


def style():
    return """
    <style>
        table, th, td {
          border:1px solid black;
        }
    </style>
    """


def enclose(input_to_enclose, tag):
    return "<" + tag + ">" + input_to_enclose + "</" + tag + ">"


def tr(input):
    return "<tr>" + input + "</tr>"


def th(input):
    return "<th>" + input + "</th>"


def heading_text():
    return "<h1>Downtimes</h1>"


def download_heartbeat():
    return "<a href=http://" + IPAddr + ":8080/heartbeatfile download>download hearbeat file</a>"


def download_downtimes():
    return "<a href=http://" + IPAddr + ":8080/downtimesfile download>download downtimes file</a>"


#
# get Downtimes
#
def downtime_table():
    table = "<table><thead><th>downtime start</th><th>downtime end</th><th>time delta</th></thead>"
    if os.path.isfile(heartbeat_file_abspath) and os.path.isfile(downtimes_file_abspath):
        with open(downtimes_file_abspath, "r+") as f:
            downtimes = json.load(f)['downtimes']
            for dowtime in downtimes:
                table += tr(th(dowtime['shutdown']) + th(dowtime['startup']) + th(dowtime['delta']))
    else:
        table += tr(th("no data") + th("no data") + th("no data"))

    return table


@app.route('/')
def hello():
    prolog = enclose(heading_text(), "div")
    table = enclose(downtime_table(), "div")
    download = enclose(download_heartbeat(), "div") + enclose(download_downtimes(), "div")
    return enclose(style() + enclose(prolog + table + download, "body"), "html")


@app.route('/heartbeatfile')
def return_hearbeat_file():
    try:
        return send_file(heartbeat_file_abspath)
    except Exception as e:
        return str(e)


@app.route('/downtimesfile')
def return_downtimes_file():
    try:
        return send_file(downtimes_file_abspath)
    except Exception as e:
        return str(e)


app.run(host='0.0.0.0', port=8080)
