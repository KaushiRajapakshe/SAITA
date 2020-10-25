import os
import re

import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.phrases as phrases
from SAITA.IT16178700.abstracterror import error_detail
from SAITA.IT16178700.data.log import add_log, log_types
from SAITA.IT16178700.model.Error import Error
from SAITA.IT16178700.GUI.GuiPopupWindow import GuiPopupWindow


# GET log file list for stack trace and error identify
def get_log_file():
    log_files = [access_file_detail.view_log_details("../textfile/logExtension.txt"),
                 access_file_detail.view_log_details("../textfile/logMatch.txt"),
                 access_file_detail.view_log_details("../textfile/logNoExtension.txt")]  # set logs txt file list
    return log_files


# Preventing scanner stack trace identify
def identify_stack_trace(work_area, acc_ra, roott):
    # Define stack trace important list variable
    important = []
    # Define stack trace list variable
    stack_trace = []

    # key phrases
    keep_phrases = phrases.get_phrases()
    # regular expression patterns
    regular_expression1 = phrases.get_regular_expression1()
    expression1 = re.compile(regular_expression1)
    regular_expression2 = phrases.get_regular_expression2()
    expression2 = re.compile(regular_expression2)
    # Define count variable as 0
    count = 0
    # Define log file length variable as 0
    length = 0
    # Define error list variable
    error_list = []
    # Define string phrase variable
    set_phrase = ''
    # Define string log variable
    set_log = ''
    # identify stack trace on error
    c = get_log_file()
    # Apply loading for identify logs with .log extension scanner
    maxp = 0
    for logs in c:
        for infile in logs:
            maxp += len(infile)
    ma = "Scanning ..."
    massage = GuiPopupWindow(roott,
                             acc_ra,
                             work_area,
                             "Log file reading",
                             [ma],
                             [0.4615, 0.35, 0.2702, 5],
                             type="download",
                             close=False,
                             )
    k = 0
    massage.top.deiconify()
    massage.progress["value"] = 0
    maxsi = maxp
    massage.progress["maximum"] = maxsi

    showt = 1
    # Identify Stack trace by reading log files
    for logs in c:

        for infile in logs:
            for log in infile:
                last_char = infile[-1]
                if last_char == "\n":
                    infile = infile[:-1]
                last_ch = log[-1:]
                if last_ch == "\n":
                    log = log[:-1]
                # See if the path exists.
                if os.path.exists(log):
                    # open file
                    try:
                        with open(log, 'r') as f:
                            f = f.readlines()
                            error = Error()
                            for line in f:
                                length += 1
                                if expression1.search(line) or length == len(f) or expression2.search(line):
                                    if count == 1:
                                        # If count = 1 set Error details for Error and ESubDetail Model and
                                        # count changed to 0 and stack trace equal to empty
                                        count = 0
                                        important.append(stack_trace)
                                        error.set_log_stack_trace(stack_trace)
                                        error.set_error_description(set_phrase)
                                        error.set_log_path(set_log)
                                        error_list = check_error_list(error, error_list)
                                        error_detail.error_details(stack_trace, log)
                                        stack_trace = []
                                    stack_trace = [line]
                                else:
                                    stack_trace.append(line)
                                # Check phrases having on error log file line
                                for phrase in keep_phrases:
                                    if phrase in line:
                                        # If true set phrase, log and count = 1
                                        set_phrase = phrase
                                        set_log = log
                                        count = 1
                        length = 0
                        # error_list.append(error)
                    except (IOError, PermissionError, UnicodeDecodeError) as e:
                        add_log(log_types[0], "Stack Trace Identify : ", e)
                        pass
                done = round((100 * k / showt), 1)
                k += 1
                showt = maxsi
                massage.progress["value"] = round(k)
                massage.progress_num.config(text=str(done) + " %")
                massage.filecount.config(text="Files : " + str(k) + " / " + str(maxsi))
                massage.top.update()
    # Destroy loading window after completing the loop
    massage.top.destroy()

    # Set scanner log error details in SAITA log path
    for p in important:
        for line in p:
            add_log(log_types[2], "Stack Trace Identify : ", line)
        add_log(log_types[2], "Stack Trace Identify : ", '############################################################')
    return error_list


# Check error list for stack trace on scheduler
def check_error_list(error, error_list):
    count = 0
    log_true = 1
    if not error_list:
        error_list.append(error)
    else:
        for e in error_list:
            count += 1
            if e.get_log_path() in error.get_log_path() and e.get_error_description() in error.get_error_description():
                log_true = 2
            elif log_true != 2 and len(error_list) == count:
                error_list.append(error)
    return error_list
