import os
from fnmatch import fnmatch

import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.scheduler.drives_list as drives_list

pattern = "*log"
log_no_extension = []


def get_log_no_extension():
    for root in drives_list.get_os_drives_list():
        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    log_no_extension.append(os.path.join(path, name))
    return log_no_extension


all_output_list = ['\n'.join(get_log_no_extension())]

access_file_detail.add_log_details(all_output_list, "../textfile/logNoExtension.txt")
