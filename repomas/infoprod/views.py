import requests
from flask import render_template
from requests.auth import HTTPBasicAuth

from . import info

@info.route('/info/facilities', methods=['GET'])
def facilities():
    req = requests.get("https://play.dhis2.org/demo/api/33/dataSets/EDzMBk0RRji",
        auth=HTTPBasicAuth('admin', 'district'))

    
    if req.status_code == 200:
        pass
    print(req.status_code)
    return render_template('info/facilities.html', title="Facilities")







