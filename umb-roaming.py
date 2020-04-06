#!/usr/bin/env python
"""

UMBRULLA ROAMING DEVICE RENAME


Copyright (c) 2018-2020 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import requests
import json
import sys
import base64

# API keys:
# https://dashboard.umbrella.com/o/<orgid>/#/admin/apikeys

key='yyy'
secret='xxx'
orgid="1111111"

#https://docs.umbrella.com/umbrella-api/docs/authenticating-api-requests
#  apiKey:apiSecret
#  This is then base64 encoded, and used in the Authorization header following the word “Basic”.

#
#  List the roaming computers
#
print("Roaming devices:")
key2=key+':'+secret
encoded = base64.b64encode(key2.encode())
apikey='Basic '+encoded.decode("utf-8")
header={'Authorization' :apikey,'Content-Type':'application/json'}
devices=requests.get(f"https://management.api.umbrella.com/v1/organizations/{orgid}/roamingcomputers",headers=header)
print(json.dumps(devices.json(),indent=4,sort_keys=True))

#
#  List a given roaming computer
#
dev_id=input("ID of the Device:")
dev = requests.get(f"https://management.api.umbrella.com/v1/organizations/{orgid}/roamingcomputers/{dev_id}",headers=header)
dev_json=dev.json()
print(json.dumps(dev_json,indent=4,sort_keys=True))

#
#  Change the name of a given roaming computers
#
dev_new_name=input("New name of the Device:")
new_name= {"name": dev_new_name}
resp = requests.put(f"https://management.api.umbrella.com/v1/organizations/{orgid}/roamingcomputers/{dev_id}", data=json.dumps(new_name), headers=header)
if resp.status_code == 200:
	print("Rename was successful. Please wait a few minutes and refresh the page!")
else:	
	print(f"***** Rename was NOT successful! *****, status_code:{resp.status_code}")



