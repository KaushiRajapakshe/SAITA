from ARTA.error.analysis.scheduler.logidentity import log_path
from ARTA.model import Error
from ARTA.model import ESubDetail


# Set Error Module data
#     stack_trace
#     application_name
#     application_path
# Set ESubDetail Module data
#     action
def error_details(stack_trace, infile):
    Error._log_stack_trace = stack_trace
    Error.application_name = get_application_name(infile)
    Error.application_path = infile
    ESubDetail.action = stack_trace


# Get Application Name by log path
def get_application_name(infile):
    for head_dir in log_path.get_log_path_list():
        if head_dir in infile:
            path = infile
            list_line = path.split('/')
            return list_line[2]
