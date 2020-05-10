import os
from fnmatch import fnmatch

import access_file_detail
from logidentity import log_path

pattern = "*log"
log_no_extension = []


def get_log_no_extension():
    for root in log_path.get_log_path_list():
        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    log_no_extension.append(os.path.join(path, name))
    return log_no_extension


all_output_list = ['\n'.join(get_log_no_extension())]

access_file_detail.add_log_details(all_output_list, "../textfile/logNoExtension.txt")
