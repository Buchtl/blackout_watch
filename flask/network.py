import netifaces as ni
import logging
import sys
import re
import time

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
def get_ip(pattern: str, delay: int):
    result = ""
    while not re.search(pattern, result):
        for interface in ni.interfaces():
            addr = str(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
            if re.search(pattern, addr):
                result = addr
                logger.debug("Pattern " + pattern + " matches " + addr)
        if not result:
            logger.debug("No matching interface yet. Waiting " + delay.__str__() + " seconds for next approach.")
            time.sleep(delay)

    return result


pattern = "192.{3}[0-9].[0-9]{1,3}"
logger.debug(" ip is " + get_ip(pattern, 5))
