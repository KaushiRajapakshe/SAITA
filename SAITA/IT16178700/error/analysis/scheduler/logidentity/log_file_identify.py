import os
from SAITA.IT16178700.constant import constants
import SAITA.IT16178700.access_file_detail as access_file_detail
from SAITA.IT16178700.error.analysis.scheduler import drives_list


def dir_list_folder():
    output_list = []
    for head_dir in drives_list.get_os_drives_list():
        for root, dirs, files in os.walk(head_dir):
            for d in dirs:
                if d.upper() == constants.CAPITAL_LOGS.upper():
                    output_list.append(os.path.join(root, d))
                if d.upper() == constants.SIMPLE_LOGS.upper():
                    output_list.append(os.path.join(root, d))
    return output_list

# MAC Implementation
# def dir_list_folder(head_dir, dir_name):
#     output_list = []
#     for root, dirs, files in os.walk(head_dir):
#         for d in dirs:
#             if d.upper() == dir_name.upper():
#                 output_list.append(os.path.join(root, d))
#     return output_list


def add_log_match_file():
    all_output_list = ['\n'.join(dir_list_folder())]

    access_file_detail.add_log_details(all_output_list, "../textfile/logMatch.txt")
