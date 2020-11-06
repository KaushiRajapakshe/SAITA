import requests

from SAITA.IT16178700.data import variables


# OWL File Upload for Apache Jena Fuseki Server
def upload_owl():
    url = variables.url + '/data'
    # Open OWL file
    data = open(variables.ontology_path).read()
    headers = {'Content-Type': 'application/rdf+xml; boundary=----WebKitFormBoundaryc8DYiSwZQFPx4yH1'}
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == 200:
        return 'Success'
    else:
        return 'Fail'


# upload owl file
if __name__ == "__main__":
    result = upload_owl()
    print("OWL File Upload : ", result)
