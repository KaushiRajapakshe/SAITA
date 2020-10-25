from SAITA.IT16178700.config import config_controller
from SAITA.IT16178700.data.log import add_log, log_types
from SAITA.IT16178700.error.analysis.scheduler import stack_trace_identify
from SAITA.IT16178700.error.analysis.scheduler.logidentity import log_no_extension, log_extension_identify, \
    log_file_identify
from SAITA.IT16178700.ontology import query
from SAITA.IT16178700.controllers.ontology import query_controller
import re


# Preventing Scanner run for identify logs
#     with file names
#     with file extension
#     with folder name
# Those identified logs read and identify errors
# scanning by lines
# Also preventing scanner identify
# error stack trace
def scanner_details(work_area, acc_ra, roott):
    # initialise config object using the config_controller
    app_config = config_controller.init_config("../app.ini")

    # get string value scheduler_log_scan
    scheduler_log_scan = app_config.get('default', 'scheduler_log_scan')

    # check application property
    if scheduler_log_scan == 'enable':
        # Log identify module
        log_file_identify.add_log_match_file(work_area, acc_ra, roott)
        log_extension_identify.add_log_extension(work_area, acc_ra, roott)
        log_no_extension.add_log_no_extension_file(work_area, acc_ra, roott)
    # Identify stack trace and error details
    error_list = stack_trace_identify.identify_stack_trace(work_area, acc_ra, roott)

    # Get Application list from knowledge base
    query_type = query.get_application_type()
    application_list = query_controller.execute_query(query_type)

    # Define Scanner list dictionary to store application error details with log data
    scanner_list = {}
    # Set list = 0 and it will iterate once have data
    i = 0

    for ap_name in application_list:
        for e in error_list:
            error_value = ap_name + ' Application : ' + e.get_error_description()
            if len(scanner_list) == 0:
                if re.search(r'\b' + ap_name + '\\b', e.get_log_path(), re.IGNORECASE):
                    i += 1  # Iterating key set value for scanner list dictionary
                    scanner_list[i] = '[' + str(i) + ']  ' + error_value
            else:
                # Remove redundant log errors
                for error in scanner_list.values():
                    if not re.search(r'\b' + error_value, error):
                        # verify logs error data with knowledge base data
                        if re.search(r'\b' + ap_name + '\\b', e.get_log_path(), re.IGNORECASE):
                            i += 1  # Iterating key set value for scanner list dictionary
                            scanner_list[i] = '[' + str(i) + ']  ' + error_value

    add_log(log_types[2], "Scanner : ", str(scanner_list))
    return scanner_list
