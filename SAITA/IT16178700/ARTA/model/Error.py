# SAITA Pre selected Application related issue solving Agent
# Error Model class

class Error:
    # Error Class Attributes
    type: 'log error'

    # Initializer / Instance Attributes
    def __init__(self):
        self._error_id = ''
        self._error_description = ''
        self._application_name = ''
        self._application_path = ''
        self._application_version = ''
        self._log_stack_trace = ''
        self._log_path = ''

    # getter method error_id
    def get_error_id(self):
        return self._error_id

    # setter method error_id
    def set_error_id(self, error_id):
        self._error_id = error_id

    # getter method error_description
    def get_error_description(self):
        return self._error_description

    # setter method error_description
    def set_error_description(self, error_description):
        self._error_description = error_description

    # getter method application_name
    def get_application_name(self):
        return self._application_name

    # setter method application_name
    def set_application_name(self, application_name):
        self._application_name = application_name

    # getter method application_path
    def get_application_path(self):
        return self._application_path

    # setter method application_path
    def set_application_path(self, application_path):
        self._application_path = application_path

    # getter method application_version
    def get_application_version(self):
        return self._application_version

    # setter method application_version
    def set_application_version(self, application_version):
        self._application_version = application_version

    # getter method log_stack_trace
    def get_log_stack_trace(self):
        return self._log_stack_trace

    # setter method log_stack_trace
    def set_log_stack_trace(self, log_stack_trace):
        self._log_stack_trace = log_stack_trace

    # getter method log_path
    def get_log_path(self):
        return self._log_path

    # setter method log_path
    def set_log_path(self, log_path):
        self._log_path = log_path

