import json
import getpass
import os.path
import socket
from datetime import datetime
from datetime import timedelta

path_home = "/home/" + getpass.getuser() + "/"
heartbeat_file_abspath = path_home + "heartbeat.txt"
downtimes_json = path_home + "downtimes.json"
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

# get last heartbeat as date
def getLastHeartbeat():
    with open(heartbeat_file_abspath) as f_ping:
        lines = f_ping.readlines()
        for line in lines:
            pass
        last_heartbeat = int("".join(c for c in line if c.isdigit()))
    return datetime.strptime(last_heartbeat.__str__(), '%Y%m%d%H%M')

if os.path.isfile(heartbeat_file_abspath):
    last_heartbeat = getLastHeartbeat()
else:
    exit(0)

current = datetime.now()
delta = (current - last_heartbeat) / timedelta(minutes=1)
element = {'shutdown': last_heartbeat.__str__(), 'startup': current.strftime("%Y-%m-%d %H:%M:%S").__str__(), 'delta': delta.__str__()}

data = [element]
if not os.path.isfile(downtimes_json):
    with open(downtimes_json, "x") as f:
        json.dump({'downtimes': [element]}, f, indent=4)
else:
    with open(downtimes_json, "r+") as f:
        json_content = json.load(f)
        print(json_content)
        print("##################")
        json_content['downtimes'].append(element)
        print("updated")
        print(json_content)
        with open(downtimes_json, "w") as f_out:
            json.dump(json_content, f_out, indent=4)

exit(0)