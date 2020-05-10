from DBConnection import DBConnection


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
        return cls.mydb.select_param_query('SELECT tech_solution FROM network_issues where issue_id=%s', (issue_id,))

    @classmethod
    def get_nontech_solution_id_by_issue_id(cls, issue_id):
        return cls.mydb.select_param_query('SELECT nontech_solution FROM network_issues where issue_id=%s', (issue_id,))
