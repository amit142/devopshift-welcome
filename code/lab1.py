import logging
import os
import sys
import json

class JsonFormatter(logging.Formatter):
    def format(self, record) :
      log = {
            "time": record.created,
            "module": record.module,
            "level": record.levelname,
            "message": record.getMessage()
        }
      return json.dumps(log)
log_level = os.environ.get("LOG_LEVEL", "DEBUG").upper()
log_format = os.environ.get("LOG_FORMAT", "TEXT").upper()
logger = logging.getLogger("amit-app")
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(log_level)
if log_format == 'JSON':
    handler.setFormatter(JsonFormatter())
else:
    log_format = logging.Formatter("%(ascitime)s:%(name)s:%(levelname)s:%(massage)s")
logger.addHandler(handler)


logger.setLevel(log_level)    

#logging.basicConfig(filename="myapp.log",format=log_format,level=log_level)


server_list = ["server1", "server2", "server3"]
servers = {"server1": "on", "server2": "off", "server3": "on"}

while True:
    x = input("Enter the server name: ")

    # Check if the server exists in the dictionary
    if x not in servers:
        # If server is not found, log an error and continue the loop
        logger.error(f"Server '{x}' does not exist. Choose from {server_list}.")
    else:
        # If the server is found, log info and print its status
        logger.info(f"Server '{x}' is {servers[x]}")
        print(f"{x} is {servers[x]}")