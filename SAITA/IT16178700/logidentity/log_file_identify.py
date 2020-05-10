import os
from constant import constants
import access_file_detail


def dir_list_folder(head_dir, dir_name):
    output_list = []
    for root, dirs, files in os.walk(head_dir):
        for d in dirs:
            if d.upper() == dir_name.upper():
                output_list.append(os.path.join(root, d))
    return output_list


all_output_list = ['\n'.join(dir_list_folder(r'' + constants.FOLDER_NAME_APPLICATIONS, constants.SIMPLE_LOGS)),
                   '\n'.join(dir_list_folder(r'' + constants.FOLDER_NAME_USERS, constants.CAPITAL_LOGS)),
                   '\n'.join(dir_list_folder(r'' + constants.FOLDER_NAME_LIBRARY, constants.CAPITAL_LOGS))]

access_file_detail.add_log_details(all_output_list, "../textfile/logMatch.txt")