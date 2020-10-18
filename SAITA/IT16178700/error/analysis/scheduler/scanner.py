from SAITA.IT16178700.error.analysis.scheduler import stack_trace_identify
from SAITA.IT16178700.error.analysis.scheduler.logidentity import log_no_extension, log_extension_identify, \
    log_file_identify
from SAITA.IT16178700.ontology import query
from SAITA.IT16178700.controllers.ontology import query_controller
import re


def scanner_details():
    log_extension_identify.add_log_extension()
    log_file_identify.add_log_match_file()
    log_no_extension.add_log_no_extension_file()
    error_list = []
    error_list = stack_trace_identify.identify_stack_trace()

    query_type = query.get_application_type()
    application_list = query_controller.execute_query(query_type)

    scanner_list = {}
    i = 0

    for ap_name in application_list:
        for e in error_list:
            if re.search(r'\b' + ap_name + '\\b', e.get_log_path(), re.IGNORECASE):
                i += 1
                scanner_list[i] = '[' + str(i) + ']  ' + ap_name + ' Application : '+ e.get_error_description()

    print(scanner_list)
    return scanner_list

