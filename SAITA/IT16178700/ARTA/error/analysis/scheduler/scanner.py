from ARTA.config import config_controller
from ARTA.data import validate, variables
from ARTA.data.log import add_log, log_types
from ARTA.error.analysis.scheduler import stack_trace_identify
from ARTA.error.analysis.scheduler.logidentity import log_no_extension, log_extension_identify, \
    log_file_identify
from ARTA.error.analysis.userentered.application_path_identify import check_application_port
from ARTA.ontology import query
from ARTA.controllers.ontology import query_controller
import re
import copy

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
    app_config = config_controller.init_config(variables.scanner_config_path)

    # get string value scheduler_log_scan
    scheduler_log_scan = app_config.get('log', 'scheduler_log_scan')

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
    application_list.append('Protege')

    # Define Scanner list dictionary to store application error details with log data
    scanner_list = {}
    # Set list = 0 and it will iterate once have data
    i = 0

    error_list_class = []

    for ap_name in application_list:
        for e in error_list:
            if re.search(r'\b' + ap_name + '\\b', e.get_log_path(), re.IGNORECASE):
                error_value = ap_name + ' Application : ' + e.get_error_description()
                e.set_error_description(error_value)
                e.set_application_name(ap_name)
                # using deepcopy o deep copy
                error = copy.deepcopy(e)
                error_list_class.append(error)
                i += 1  # Iterating key set value for scanner list dictionary
                scanner_list[i] = error_value

    error_scan_list = append_error_class_details(error_list_class)

    scanner_list1 = remove_redundant_value(error_scan_list)
    add_log(log_types[2], "Scanner : ", str(scanner_list1))
    return scanner_list1


def remove_redundant_value(error_scan_list):
    # Define Scanner and Error list to store application error details with log data
    error_list_without_dup = []

    # Set list = 0 and it will iterate once have data
    i = 0
    for e in error_scan_list:
        if len(error_list_without_dup) == 0:
            i += 1  # Iterating key set value for scanner list
            # using deepcopy o deep copy
            error = copy.deepcopy(e)
            error.set_error_description('[' + str(i) + ']  ' + e.get_error_description())
            error_list_without_dup.append(error)
        else:
            for err in error_list_without_dup:
                if not re.search(r'\b' + e.get_error_description() + '\\b', err.get_error_description(), re.IGNORECASE):
                    i += 1  # Iterating key set value for scanner list
                    # using deepcopy o deep copy
                    er = copy.deepcopy(e)
                    er.set_error_description('[' + str(i) + ']  ' + e.get_error_description())
                    error_list_without_dup.append(er)

    return error_list_without_dup


def append_error_class_details(error_list_class):
    for e in error_list_class:
        # print(e.get_log_path(), e.get_error_description(), e.get_application_name(), e.get_log_stack_trace())
        for r in validate.data_validate:
            if re.search(r'\b' + r[0] + '\\b', e.get_error_description(), re.IGNORECASE):
                stack_trace = e.get_log_stack_trace()
                for line in stack_trace:
                    if re.search(r'\b' + r[1] + '\\b', line, re.IGNORECASE):
                        e.set_application_version(line)
                        if validate.data_validate[0][1] == r[1]:
                            e.set_application_path('none')
                            # Check valid port range
                            if check_application_port(line, e) == 'True':
                                pass
    return error_list_class
