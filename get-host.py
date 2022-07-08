import json
import requests
api_url = "http://localhost:58000/api/v1/host"

headers = {'content-type':'application/json','X-Auth-Token':"NC-12-6fa26fc327d740e1a9da-nbi"}

resp = requests.get(api_url, headers=headers, verify=False, params="")

print("Request status: ", resp.json())

response_json = resp.json()
hosts = response_json["response"]

#for host in hosts:
#    print(int(host["hostName"]))