import requests
# from flask import jsonify
from requests.auth import HTTPBasicAuth


# req = requests.get("https://play.dhis2.org/demo/api/33/dataValueSets",
#  auth=HTTPBasicAuth('admin', 'district'))

req = requests.get("https://play.dhis2.org/demo/api/33/dataSets/EDzMBk0RRji",
 auth=HTTPBasicAuth('admin', 'district'))


if req.status_code == 200:
    for
print(req.status_code)
