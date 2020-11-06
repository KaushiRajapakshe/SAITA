# SAITA Pre selected Application related issue solving Agent
# ESubDetail Model class

class ESubDetail:
    type: 'error details'

    def __init__(self):
        self._error_id = ''
        self._error_category = ''
        self._pid = ''
        self._action = ''
        self._solution = ''
        self._final_resolution = ''

    # self._owner_name = owner_name
    # getter method error_id
    def get_error_id(self):
        return self._error_id

    # setter method error_id
    def set_error_id(self, error_id):
        self._error_id = error_id

    # getter method error_category
    def get_error_category(self):
        return self._error_category

    # setter method error_category
    def set_error_category(self, error_category):
        self._error_category = error_category

    # getter method pid
    def get_pid(self):
        return self._pid

    # setter method pid
    def set_pid(self, pid):
        self._pid = pid

    # getter method action
    def get_action(self):
        return self._action

    # setter method action
    def set_action(self, action):
        self._action = action

    # getter method solution
    def get_solution(self):
        return self._solution

    # setter method solution
    def set_solution(self, solution):
        self._solution = solution

    # getter method final_resolution
    def get_final_resolution(self):
        return self._final_resolution

    # setter method final_resolution
    def set_final_resolution(self, _final_resolution):
        self._final_resolution = _final_resolution
