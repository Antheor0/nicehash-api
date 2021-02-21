#/bin/Python3
#Nicehas API

#Code de clé API:
#1bdba85a-27d0-4e5b-bef8-a4131228d1a2

#Api Code de clé Secrète:
#e66a81ac-36a6-478b-9ff1-6b9fbcd9a92d422cd9cf-ad1e-48b4-b9dc-9593ff8899f3
#Import modules
import requests
import hmac
import hashlib
from datetime import datetime
from time import mktime
import uuid
def get_epoch_ms_from_now():
    now = datetime.now()
    now_ec_since_epoch = mktime(now.timetuple()) + now.microsecond / 1000000.0
    return int(now_ec_since_epoch * 1000)

def get_request(nicehashUrl,mainUrl,endUrl,param,apiKey,apiSecret,organizationId):

    dataxtime = requests.get("https://api2.nicehash.com/api/v2/time")
    xtime = dataxtime.json()['serverTime']
    url= mainUrl + endUrl
    fullurl = nicehashUrl + url +
    xnonce = str(uuid.uuid4())
    method = "GET"

    message = bytearray(apiKey, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(str(xtime), 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(xnonce, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(organizationId, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(method, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(url, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(param, 'utf-8')

    print(message)
    signature = hmac256gen(apiSecret,message)
    xauth = apiKey+":"+signature

    headers = {'X-Time': str(xtime),
    'X-Nonce':xnonce,
    'X-Organization-Id':organizationId,
    'Content-Type': 'application/json',
    'X-Request-Id':str(uuid.uuid4()),
    'X-Auth': xauth
    }
    print(headers)
    s = requests.Session()
    s.headers = headers
    response = s.request(method, fullurl)

    if response.status_code == 200:
        return response.json()
    elif response.content:
        raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
    else:
        raise Exception(str(response.status_code) + ": " + response.reason)


def hmac256gen(apiKey,message):
    signature = hmac.new(bytearray(apiKey, 'utf-8'), message, hashlib.sha256).hexdigest()
    return signature


nicehashUrl = "https://api2.nicehash.com"
mainUrl = "/main/api/v2/"
#apiKey = "1bdba85a-27d0-4e5b-bef8-a4131228d1a2"
#apiSecret = "e66a81ac-36a6-478b-9ff1-6b9fbcd9a92d422cd9cf-ad1e-48b4-b9dc-9593ff8899f3"
#organizationId = "1a83239e-13e4-4cdd-8967-3c63f7acce7a"

apiKey = "666c051e-5ae1-4405-a7f7-a8dcf0c5adda"
apiSecret = "7e515cf1-bfac-4765-b990-ac3cd458fb5e6cb2f85a-afdd-4aa8-be62-1b6b61bebd86"
organizationId = "7f4f59d5-e134-4cfd-90ef-0dfe2756f23c"
rigId =  "0-UGhgnHV5cV+6Sg04XnDvrw"
endUrl = "mining/rig2/"



response = get_request(nicehashUrl,mainUrl,endUrl,rigId,apiKey,apiSecret,organizationId)
print(response)
