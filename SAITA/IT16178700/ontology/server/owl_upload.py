import requests

from SAITA.IT16178700.data import variables


def uploadOWL():
    url = variables.url + '/data'
    data = open('../../ontology/saita.owl').read()
    headers = {'Content-Type': 'application/rdf+xml; boundary=----WebKitFormBoundaryc8DYiSwZQFPx4yH1'}
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == 200:
        return 'Success'
    else:
        return 'Fail'

