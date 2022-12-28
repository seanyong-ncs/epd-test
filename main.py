import requests
import json
import time



def change_status():

    url = "https://ncs-srb-001.dynv6.net:1880/errorCode.do"
    payload = json.dumps({
    "dataList": [
        {
        "errorCode": 312,
        "errorStatus": 0
        }
    ],
    "idCode": "865553058996000",
    "time": 1671501357000
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)

def throw_trash(percentage):

    range = -percentage + 155
    url = "https://ncs-srb-001.dynv6.net:1880/throwTrash.do?garbageIndex=1&type=3"

    payload = json.dumps({
    "dataList": [
        {
        "garbageIndex": 1,
        "type": 9,
        "weight": 10101,
        "beforeWeight": 1434,
        "afterWeight": 1441,
        "range": range
        }
    ],
    "idCode": "864622110032548",
    "idContent": "1234567890",
    "idType": 7,
    "time": int(time.time() * 1000)
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

if __name__ == '__main__':

    print(int(time.time() * 1000))
    print("Setting fill to 50%")
    throw_trash(50)
    # print("Sleeping for 120 seconds...")
    # sleep(120)
    
    # print("Setting fill to 90%")
    # throw_trash(90)
    # print("Sleeping for 120 seconds...")
    # sleep(120)
    
    # print("Setting fill to 15%")
    # throw_trash(15)
