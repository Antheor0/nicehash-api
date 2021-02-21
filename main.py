import nicehash
import json
import os
import sys
import threading
import time
from subprocess import call

def write_file(path,file,message):
    pathsys=os.path.dirname(sys.argv[0])
    os.chdir(path)
    file = open(file, "w")
    file.write(message)
    file.close()
    os.chdir(pathsys)

def thread_second():
    call(["python3", "server.py"])

#Setting working directory
print("Setting up working directory")
print(os.path.dirname(sys.argv[0]))
os.chdir(os.path.dirname(sys.argv[0]))

#Starting web server
print("Starting web server")
processThread = threading.Thread(target=thread_second)  # <- note extra ','
processThread.start()

#Getting env variables
apiKey = os.environ["api_key"]
apiSecret = os.environ["api_secret"]
organizationId = os.environ["organization_id"]

host = "https://api2.nicehash.com"
#setting up scrape time
scrapeInterval = "15"

#golder to save data scrapped from the api
dataPath="data"

#path of the request in the api
path = "/main/api/v2/mining/rigs"
private_api = nicehash.private_api(host, organizationId, apiKey, apiSecret)
while True:
    response = private_api.request("GET", path , '' , None )
    result=json.dumps(response, indent=4, sort_keys=True)
    write_file(dataPath,"rig.json",result)
    time.sleep(scrapeInterval)
