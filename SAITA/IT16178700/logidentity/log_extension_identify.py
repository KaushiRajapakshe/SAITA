import SAITA.IT16178700.access_file_detail as access_file_detail
from SAITA.IT16178700.logidentity import log_path

log_extension = []


def get_log_extension():
    for head_dir in log_path.get_log_path_list():
        import os
        for root, dirs, files in os.walk(head_dir):
            for file in files:
                if file.endswith(".log"):
                    log_extension.append(os.path.join(root, file))
    return log_extension


all_output_list = ['\n'.join(get_log_extension())]
access_file_detail.add_log_details(all_output_list, "../textfile/logExtension.txt")
