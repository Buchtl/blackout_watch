import json
import getpass
import os.path
import socket
from datetime import datetime
from datetime import timedelta
import logging

path_home = "/home/" + getpass.getuser() + "/"
heartbeat_file_abspath = path_home + "heartbeat.txt"
downtimes_json = path_home + "downtimes.json"
logfile = path_home + "startup.log"
logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)s %(message)s')
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

logging.info("Check for downtime")


# get last heartbeat as date
def get_last_heartbeat():
    with open(heartbeat_file_abspath) as f_ping:
        lines = f_ping.readlines()
        for line in lines:
            pass
        last_heartbeat_str = int("".join(c for c in line if c.isdigit())).__str__()
    return datetime.strptime(last_heartbeat_str.__str__(), '%Y%m%d%H%M')


if os.path.isfile(heartbeat_file_abspath):
    last_heartbeat = get_last_heartbeat()
    logging.debug("latest hearbeat is " + last_heartbeat.__str__())
else:
    logging.info("File " + heartbeat_file_abspath + " doesn't exist -> exit")
    exit(0)

current = datetime.now()
logging.debug("current time is " + current.strftime("%Y-%m-%d %H:%M:%S").__str__())
delta = current - last_heartbeat
element = {'shutdown': last_heartbeat.__str__(), 'startup': current.strftime("%Y-%m-%d %H:%M:%S").__str__(),
           'delta': delta.__str__()}

data = [element]
if not os.path.isfile(downtimes_json):
    logging.debug(downtimes_json + " does not exist -> creating it")
    with open(downtimes_json, "x") as f:
        json.dump({'downtimes': [element]}, f, indent=4)
else:
    logging.debug("appending downtime to " + downtimes_json)
    with open(downtimes_json, "r+") as f:
        json_content = json.load(f)
        json_content['downtimes'].append(element)
        with open(downtimes_json, "w") as f_out:
            json.dump(json_content, f_out, indent=4)

exit(0)
