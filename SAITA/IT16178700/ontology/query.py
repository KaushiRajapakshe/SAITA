from SAITA.IT16178700.constant import constants


def query_by_application_name(value, application_name):
    query1 = """
        PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

        SELECT ?application_name ?error_description ?application_version ?error_action WHERE { 
              ?saita saita:application_name ?application_name ;
                saita:error_description ?error_description ;
                saita:application_version ?application_version ;
            saita:error_action ?error_action ;
          VALUES ?""" + value + """ {'""" + application_name + """'}
        }      
    """
    return query1


def get_application_type():
    query2 = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT DISTINCT ?isDefinedBy
        WHERE {
          ?rdfs rdfs:isDefinedBy ?isDefinedBy;
        }
    """
    return query2
