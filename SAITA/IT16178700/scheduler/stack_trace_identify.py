import os
import re

import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.phrases as phrases
from SAITA.IT16178700.abstracterror import error_detail


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

    # identify stack trace on error
    for logs in get_log_file():
        for infile in logs:
            for log in infile:
                last_char = infile[-1]
                if last_char == "\n":
                    infile = infile[:-1]

                # See if the path exists.
                if os.path.exists(log):
                    # open file
                    try:
                        with open(log, 'r') as f:
                            f = f.readlines()
                            for line in f:
                                length += 1
                                if expression1.search(line) or length == len(f) or expression2.search(line) :
                                    if count == 1:
                                        count = 0
                                        important.append(stack_trace)
                                        error_detail.error_details(stack_trace, log)
                                        stack_trace = []
                                    stack_trace = [line]
                                else:
                                    stack_trace.append(line)
                                for phrase in keep_phrases:
                                    if phrase in line:
                                        count = 1
                        length = 0
                    except (IOError, PermissionError, UnicodeDecodeError) as e:
                        # print("Error : ", e) // want to write log
                        pass

    for p in important:
        for line in p:
            print(line)
        print(
            '##########################################################################################################')
