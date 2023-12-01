from flask import Flask
import getpass
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)

@app.route('/')
def hello():
    path = "/home/" + getpass.getuser() + "/ping.txt"
    print(path)
    values = []
    response = ""
    with open(path) as f_ping:
        lines = f_ping.readlines()
        for line in lines:
            values.append(int(line.replace("\n", "")))

    response += "Messpunkte: " + len(values).__str__() + "</br>"
    count = 0
    for value in values:
        if count > 0:
            offset = value - values[count - 1]
            if offset > 2:
                date_before = datetime.strptime(values[count - 1].__str__(), '%Y%m%d%H%M')
                date_after = datetime.strptime(value.__str__(), '%Y%m%d%H%M')
                delta = (date_after - date_before) / timedelta(minutes=1)
                response += "Ausfall zwischen " + date_before.__str__() + " und " + date_after.__str__() + " von " + delta.__str__() + " Minuten</br>"
        count+=1

    return response

app.run(host='0.0.0.0', port=8080)