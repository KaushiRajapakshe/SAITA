import os
import re

import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.phrases as phrases
from SAITA.IT16178700.abstracterror import error_detail
from SAITA.IT16178700.model.Error import Error


def get_log_file():
    log_files = [access_file_detail.view_log_details("../textfile/logExtension.txt"),
                 access_file_detail.view_log_details("../textfile/logMatch.txt"),
                 access_file_detail.view_log_details("../textfile/logNoExtension.txt")]  # set logs txt file list
    return log_files


def identify_stack_trace():
    important = []
    stack_trace = []

    # key phrases
    keep_phrases = phrases.get_phrases()
    # regular expression pattern
    regular_expression1 = phrases.get_regular_expression1()
    expression1 = re.compile(regular_expression1)
    regular_expression2 = phrases.get_regular_expression2()
    expression2 = re.compile(regular_expression2)
    count = 0
    length = 0
    error_list = []
    set_phrase = ''
    set_log = ''
    # identify stack trace on error
    for logs in get_log_file():
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
                                for phrase in keep_phrases:
                                    if phrase in line:
                                        set_phrase = phrase
                                        set_log = log
                                        count = 1
                        length = 0
                        # error_list.append(error)
                    except (IOError, PermissionError, UnicodeDecodeError) as e:
                        # print("Error : ", e) // want to write log
                        pass

    for p in important:
        for line in p:
            print(line)
        print(
            '##########################################################################################################')
    return error_list


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
                pass
            elif log_true != 2 and len(error_list) == count:
                error_list.append(error)
    return error_list
