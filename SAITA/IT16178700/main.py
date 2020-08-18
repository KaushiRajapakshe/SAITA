import os
import re

import SAITA.IT16178700.access_file_detail as access_file_detail
import SAITA.IT16178700.phrases as phrases
from SAITA.IT16178700.abstracterror import error_detail

log_files = []  # set logs txt file list
log_files = access_file_detail.view_log_details("textfile/logNoExtension.txt")

important = []
stack_trace = []

# key phrases
keep_phrases = phrases.get_phrases()
# regular expression pattern
regular_expression = phrases.get_regular_expression()
expression = re.compile(regular_expression)
count = 0
length = 0

# identify stack trace on error
for logs in log_files:
    for infile in logs:
        last_char = infile[-1]
        if last_char == "\n":
            infile = infile[:-1]
        # See if the path exists.
        if os.path.exists(infile):
            # open file
            try:
                with open(infile, 'r') as f:
                    f = f.readlines()
                    for line in f:
                        length += 1
                        if expression.search(line) or length == len(f):
                            if count == 1:
                                count = 0
                                important.append(stack_trace)
                                error_detail.error_details(stack_trace, infile)
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
    print('##########################################################################################################')

