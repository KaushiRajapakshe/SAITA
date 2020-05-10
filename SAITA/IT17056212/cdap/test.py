from Query import Queries
from DBConnection import DBConnection

x = '2'
print(DBConnection.select_query("SELECT error_msg,error_code,connection_type,issue_id FROM network_errors_msg"))
print(DBConnection.select_param_query('SELECT error_msg FROM network_errors_msg where issue_id=%s', (x,)))
print(Queries.get_errorsmsg_by_issueid(2))
print(Queries.get_all_networkerrors())