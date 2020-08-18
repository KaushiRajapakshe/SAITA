import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.scheduler.drives_list as drives_list

log_extension = []


def get_log_extension():
    for head_dir in drives_list.get_os_drives_list():
        import os
        for root, dirs, files in os.walk(head_dir):
            for file in files:
                if file.endswith(".log"):
                    log_extension.append(os.path.join(root, file))
    return log_extension


all_output_list = ['\n'.join(get_log_extension())]
access_file_detail.add_log_details(all_output_list, "../textfile/logExtension.txt")
