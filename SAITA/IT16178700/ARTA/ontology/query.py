from ARTA.constant import constants
from ARTA.data.log import add_log, log_types


# Ontology KB data extract query for SAITA Application related issue solver


# GET Application name list query
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
    add_log(log_types[2], constants.QUERY, query1)
    return query1


# GET Application type list query
def get_application_type():
    query2 = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT DISTINCT ?isDefinedBy
        WHERE {
          ?rdfs rdfs:isDefinedBy ?isDefinedBy;
        }
    """
    add_log(log_types[2], constants.QUERY, query2)
    return query2


# GET Application version list query
def get_application_version():
    query3 = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>

        SELECT DISTINCT ?versionInfo
        WHERE {
          ?owl owl:versionInfo ?versionInfo;
        }
    """
    add_log(log_types[2], constants.QUERY, query3)
    return query3


# GET Error type query
def get_error_type():
    query4 = """
        PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/>

        SELECT DISTINCT ?error_description
        WHERE {
          ?saita saita:error_description ?error_description;
        }
    """
    add_log(log_types[2], constants.QUERY, query4)
    return query4


# CHECK application version query
def check_app_version(entity, value, select):
    query5 = """
    PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

    SELECT DISTINCT ?""" + select + """ 
    WHERE { 
        ?saita saita:""" + select + """ ?""" + select + """ ;
        VALUES ?""" + entity + """ {'""" + value + """'}
        }
    """
    add_log(log_types[2], constants.QUERY, query5)
    return query5


# CHECK Error description query
def check_error_description(entity, value, select):
    query6 = """
    PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

    SELECT DISTINCT ?""" + select + """ 
    WHERE { 
        ?saita saita:""" + select + """ ?""" + select + """ ;
        VALUES ?""" + entity + """ {'""" + value + """'}
        }
    """
    add_log(log_types[2], constants.QUERY, query6)
    return query6


# GET Error action query
def get_error_action(value1, value2, value3, application_name, error_description, application_version):
    query7 = """
    PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

    SELECT  ?error_action 
    WHERE { 
        ?saita saita:application_name ?application_name ;
            saita:error_description ?error_description ;
            saita:application_version ?application_version ;
            saita:error_action ?error_action ;
            VALUES ?""" + value1 + """ {'""" + application_name + """'}.
            VALUES ?""" + value2 + """ {'""" + error_description + """'}.
            VALUES ?""" + value3 + """ {'""" + application_version + """'}.
    } 
    """
    add_log(log_types[2], constants.QUERY, query7)
    return query7


# GET Error status query
def get_error_status(value1, value2, value3, application_name, error_description, application_version):
    query8 = """
    PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

    SELECT  ?error_status 
    WHERE { 
        ?saita saita:application_name ?application_name ;
            saita:error_description ?error_description ;
            saita:application_version ?application_version ;
            saita:error_status ?error_status ;
            VALUES ?""" + value1 + """ {'""" + application_name + """'}.
            VALUES ?""" + value2 + """ {'""" + error_description + """'}.
            VALUES ?""" + value3 + """ {'""" + application_version + """'}.
    } 
    """
    add_log(log_types[2], constants.QUERY, query8)
    return query8


# GET Error target query
def get_error_target(value1, value2, value3, application_name, error_description, application_version):
    query9 = """
    PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

    SELECT  ?error_target 
    WHERE { 
        ?saita saita:application_name ?application_name ;
            saita:error_description ?error_description ;
            saita:application_version ?application_version ;
            saita:error_target ?error_target ;
            VALUES ?""" + value1 + """ {'""" + application_name + """'}.
            VALUES ?""" + value2 + """ {'""" + error_description + """'}.
            VALUES ?""" + value3 + """ {'""" + application_version + """'}.
    } 
    """
    add_log(log_types[2], constants.QUERY, query9)
    return query9


# GET Error types query
def get_error_type():
    query10 = """
    PREFIX saita: <http://www.archive.org/download/saita_20200524/saita.owl/> 

    SELECT  ?error_type
    {
	    ?saita saita:error_type ?error_type ;
    }
    """
    add_log(log_types[2], constants.QUERY, query10)
    return query10
