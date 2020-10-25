import os
from SAITA.IT16178700.constant import constants
import SAITA.IT16178700.access_file_detail as access_file_detail
from SAITA.IT16178700.error.analysis.scheduler import drives_list
from SAITA.IT16178700.GUI.GuiPopupWindow import GuiPopupWindow


# Identify System Drive List ex: C, D
# Windows Implementation
def dir_list_folder(work_area, acc_ra, roott):
    # Define log file identify path variable
    output_list = []
    for head_dir in drives_list.get_os_drives_list():

        # Apply loading for identify log file path scanner for every Driver on OS
        maxsi = 0
        showt = 1
        ma = "Scanning drive " + head_dir
        massage = GuiPopupWindow(roott,
                                 acc_ra,
                                 work_area,
                                 "Log file identity scanning...",
                                 [ma],
                                 [0.4615, 0.35, 0.2702, 5],
                                 type="download",
                                 close=False,
                                 )
        k = 0
        # Set File size for Scanner loading window
        for root, dirs, files in os.walk(head_dir):
            massage.top.deiconify()
            massage.progress["value"] = 0
            maxsi += len(files)
            massage.progress["maximum"] = maxsi
            massage.filecount.config(text="Files : " + str(k) + " / " + str(maxsi))
            for d in dirs:
                done = round((100 * k / showt), 1)
                k += 1
                showt = maxsi
                massage.progress["value"] = round(k)
                massage.progress_num.config(text=str(done) + " %")

                massage.top.update()

                # Check for Logs name
                if d.upper() == constants.CAPITAL_LOGS.upper():
                    output_list.append(os.path.join(root, d))
                # Check for logs name
                if d.upper() == constants.SIMPLE_LOGS.upper():
                    output_list.append(os.path.join(root, d))
        # Destroy loading window after completing the loop
        massage.top.destroy()
    return output_list

# MAC Implementation
# def dir_list_folder(head_dir, dir_name):
#     output_list = []
#     for root, dirs, files in os.walk(head_dir):
#         for d in dirs:
#             if d.upper() == dir_name.upper():
#                 output_list.append(os.path.join(root, d))
#     return output_list


# Write log file name list on SAITA system file
def add_log_match_file(work_area, acc_ra, root):
    all_output_list = ['\n'.join(dir_list_folder(work_area, acc_ra, root))]

    access_file_detail.add_log_details(all_output_list, "../textfile/logMatch.txt")
