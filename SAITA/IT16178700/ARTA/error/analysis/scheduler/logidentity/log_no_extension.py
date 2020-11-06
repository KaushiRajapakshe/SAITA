import os
from fnmatch import fnmatch

import ARTA.abstracterror.access_file_detail as access_file_detail
import ARTA.error.analysis.scheduler.drives_list as drives_list
from ARTA.GUI.GuiPopupWindow import GuiPopupWindow

# Set any name with log pattern for identify log files
from ARTA.data import variables

pattern = "*log"
# Define log no extension file path variable
log_no_extension = []


# Identify logs with no extension
def get_log_no_extension(work_area, acc_ra, roott):
    for root in drives_list.get_os_drives_list():

        # Apply loading for identify logs with .log extension scanner
        maxsi = 0
        showt = 1
        ma = "Scanning drive " + root

        massage = GuiPopupWindow(roott,
                                 acc_ra,
                                 work_area,
                                 "Log extension identity scanning...",
                                 [ma],
                                 [0.4615, 0.35, 0.2702, 5],
                                 type="download",
                                 close=False,
                                 )
        k = 0

        # Set File size for Scanner loading window
        for path, subdirs, files in os.walk(root):
            massage.top.deiconify()
            massage.progress["value"] = 0
            maxsi += len(files)
            massage.progress["maximum"] = maxsi
            massage.filecount.config(text="Files : " + str(k) + " / " + str(maxsi))
            for name in files:
                done = round((100 * k / showt), 1)
                k += 1
                showt = maxsi
                massage.progress["value"] = round(k)
                massage.progress_num.config(text=str(done) + " %")

                massage.top.update()
                if fnmatch(name, pattern):
                    log_no_extension.append(os.path.join(path, name))
        # Destroy loading window after completing the loop
        massage.top.destroy()
    return log_no_extension


# Write log no extension file list on SAITA system file
def add_log_no_extension_file(work_area, acc_ra, root):
    all_output_list = ['\n'.join(get_log_no_extension(work_area, acc_ra, root))]

    access_file_detail.add_log_details(all_output_list, variables.log_no_extension)
