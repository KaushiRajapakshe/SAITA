from Util.DBConnection import DBConnection


class Queries:
    mydb = DBConnection()

    @classmethod
    def get_all_networks_solution_category(cls):
        return cls.mydb.select_query('SELECT nq_one,nq_two,nq_three,nq_four,category FROM network_categorizer')

    @classmethod
    def get_all_networkerrors(cls):
        return cls.mydb.select_query('SELECT error_msg,error_code,connection_type,issue_id FROM network_errors_msg')

    @classmethod
    def get_errorsmsg_by_issueid(cls, x):
        return cls.mydb.select_param_query('SELECT error_msg FROM network_errors_msg where issue_id=%s', (x,))

    @classmethod
    def get_tech_solution_id_by_issue_id(cls, issue_id):
        return cls.mydb.select_param_query('SELECT tech_solution FROM issue_table where issue_id=%s', (issue_id,))

    @classmethod
    def get_nontech_solution_id_by_issue_id(cls, issue_id):
        return cls.mydb.select_param_query('SELECT nontech_solution FROM issue_table where issue_id=%s', (issue_id,))

    @classmethod
    def get_keywards_by_nontech_solution_id(cls, nontech_solution_id):
        return cls.mydb.select_param_query('SELECT nt_keywards FROM nontechnical_solutions where nt_id=%s',
                                           (nontech_solution_id,))

    @classmethod
    def get_permenant_parameter_by_issue_id(cls, issue_id):
        return cls.mydb.select_param_query('SELECT permenant_parameter FROM issue_table where issue_id=%s',
                                           (issue_id,))

    @classmethod
    def get_technical_solution_sequence_by_solution_id(cls, solution_id):
        return cls.mydb.select_param_query('SELECT t_steps FROM technical_solutions where t_id=%s', (solution_id,))

    @classmethod
    def get_technical_solution_parameter_status_by_cid(cls, step_id):
        return cls.mydb.select_param_query('SELECT c_para_status FROM script_commands where c_id=%s', (step_id,))

    @classmethod
    def get_technical_solution_variables_by_cid(cls, step_id):
        return cls.mydb.select_param_query('SELECT c_variable_names FROM script_commands where c_id=%s', (step_id,))

    @classmethod
    def get_technical_solution_command_by_cid(cls, step_id):
        return cls.mydb.select_param_query('SELECT c_code FROM script_commands where c_id=%s', (step_id,))

    @classmethod
    def get_technical_solution_warning_by_solution_id(cls, solution_id):
        return cls.mydb.select_param_query('SELECT t_warning FROM technical_solutions where t_id=%s', (solution_id,))

    @classmethod
    def get_all_directoryerrors(cls):
        return cls.mydb.select_query('SELECT error_msg,error_code,component_type,issue_id FROM file_errors_msg')

    @classmethod
    def get_all_directory_solution_category(cls):
        return cls.mydb.select_query('SELECT fq_one,fq_two,fq_three,fq_four,category FROM file_categorizer')

    @classmethod
    def get_all_userconferrors(cls):
        return cls.mydb.select_query('SELECT error_msg,error_code,error_type,issue_id FROM user_errors_msg')

    @classmethod
    def get_all_userconf_solution_category(cls):
        return cls.mydb.select_query('SELECT uq_one,uq_two,uq_three,uq_four,category FROM user_categorizer')
