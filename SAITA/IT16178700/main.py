import os

import access_file_details
import phrases

log_files = []
log_files = access_file_details.view_log_details("logNoExtension.txt")

important = []
keep_phrases = phrases.get_phrases()

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
                        for phrase in keep_phrases:
                            if phrase in line:
                                important.append(line)
                                break
            except IOError:
                pass

for p in important:
    print(p)
