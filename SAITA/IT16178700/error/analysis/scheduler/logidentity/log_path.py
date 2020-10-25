from SAITA.IT16178700.constant import constants


# MAC Implementation for check log path folder list
# No need to consider for windows OS
def get_log_path_list():
    log_path = [constants.FOLDER_NAME_APPLICATIONS, constants.FOLDER_NAME_LIBRARY, constants.FOLDER_NAME_USERS]
    return log_path
