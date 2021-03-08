import requests
from flask import render_template
from flask_login import login_required
from requests.auth import HTTPBasicAuth

from . import info

@info.route('/info/facilities', methods=['GET'])
@login_required
def facilities():

    facilits = []

    req = requests.get("https://play.dhis2.org/demo/api/categoryOptions.json?fields=id,organisationUnits~pluck[name]",
        auth=HTTPBasicAuth('admin', 'district'))

    if req.status_code == 200:
        facilits.append(req.json())

        
    return render_template('info/facilities.html', title="Facilities", facilits=facilits)







