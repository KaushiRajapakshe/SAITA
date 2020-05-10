from logidentity import log_path
from model import Error
from model import ESubDetail


def error_details(stack_trace, infile):
    Error._log_stack_trace = stack_trace
    Error.application_name = get_application_name(infile)
    Error.application_path = infile
    ESubDetail.action = stack_trace


# want to test for windows
def get_application_name(infile):
    for head_dir in log_path.get_log_path_list():
        if head_dir in infile:
            path = infile
            list_line = path.split('/')
            return list_line[2]
