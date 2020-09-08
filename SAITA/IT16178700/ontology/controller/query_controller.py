import requests

from SAITA.IT16178700.data import variables
from SAITA.IT16178700.ontology import query
from SAITA.IT16178700.ontology.server import owl_upload

# upload owl file
if __name__ == "__main__":
    result = owl_upload.uploadOWL()
    print("OWL File : ", result)

_application_name = "Intellij"
_application = "application_name"

# Application details
specific_query = query.query_by_application_name(_application, _application_name)

# Application names
specific_query = query.get_application_type()

# Application version
specific_query = query.get_application_version()


def execute_query():
    r = requests.post(variables.url, params={'format': 'json', 'query': specific_query})
    data = r.json()
    _list = data["results"]["bindings"]
    value = []

    for i in range(len(_list)):
        for k in _list[i]:
            value.append(_list[i][k]["value"])
    return value


print(execute_query())
