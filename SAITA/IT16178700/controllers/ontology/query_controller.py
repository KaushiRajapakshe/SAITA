import requests

from SAITA.IT16178700.data import variables
from SAITA.IT16178700.ontology import query

# Application names
specific_query = query.get_application_type()

# Application version
specific_query = query.get_application_version()


# Execute Ontology queries
#     through the Apache Jena Fuseki Server
def execute_query(query_type):
    r = requests.post(variables.url, params={'format': 'json', 'query': query_type})
    data = r.json()
    _list = data["results"]["bindings"]
    value = []

    for i in range(len(_list)):
        for k in _list[i]:
            value.append(_list[i][k]["value"])
    # return result of values from the KB
    return value


# print(execute_query())
