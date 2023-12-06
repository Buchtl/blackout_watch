import netifaces as ni
import logging
import sys
import re
import time
import subprocess


# ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = get_logger()


# Pattern = regex
# delay: time between check for ip
def get_ip(ip_pattern: str, delay: int):
    cmd = ("ip -4 -br a | egrep '%s' | awk  '{print $3}' | awk -F '/' '{print $1}'" % (ip_pattern))

    ip = ""
    while not re.search(ip_pattern, ip):
        ips = str(subprocess.check_output(cmd, shell=True, universal_newlines=True)).strip().split("\n")
        detected_ip = str
        for ip in ips:
            if re.search(ip_pattern, ip):
                detected_ip = ip
                break

        if not detected_ip:
            time.sleep(delay)
    return ip


if __name__ == "__main__":
    pattern = "192.{3}[0-9].[0-9]{1,3}.[0-9]{1,3}"
    logger.debug(" ip is " + get_ip(pattern, 5))
