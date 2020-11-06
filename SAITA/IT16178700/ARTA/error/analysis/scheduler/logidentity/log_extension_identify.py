import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.error.analysis.scheduler.drives_list as drives_list
from SAITA.IT16178700.GUI.GuiPopupWindow import GuiPopupWindow
import os

# Define log extension file path variable
from SAITA.IT16178700.data import variables

log_extension = []


# Identify logs with .log extension
def get_log_extension(work_area, acc_ra, roott):
    for head_dir in drives_list.get_os_drives_list():

        # Apply loading for identify logs with .log extension scanner
        maxsi = 0
        showt = 1
        ma = "Scanning drive " + head_dir
        massage = GuiPopupWindow(roott,
                                 acc_ra,
                                 work_area,
                                 "Log extension identity scanning... ",
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
            for file in files:

                done = round((100 * k / showt), 1)
                k += 1
                showt = maxsi
                massage.progress["value"] = round(k)
                massage.progress_num.config(text=str(done) + " %")

                massage.top.update()

                # Check .log extension files
                if file.endswith(".log"):
                    log_extension.append(os.path.join(root, file))
        # Destroy loading window after completing the loop
        massage.top.destroy()
    return log_extension


# Write log extension file list on SAITA system file
def add_log_extension(work_area, acc_ra, root):
    all_output_list = ['\n'.join(get_log_extension(work_area, acc_ra, root))]
    access_file_detail.add_log_details(all_output_list, variables.log_extension)
