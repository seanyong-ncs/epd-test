import requests
import json

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
