# Program to show various ways to read and
# write data in a file.
# append mode change "a" Append-adds at last
def add_log_details(line,file_name):
    file1 = open(file_name, "w")  #write mode
    # \n is placed to indicate EOL (End of Line)
    file1.writelines(line)
    file1.close()   # to change file access modes

def view_log_details(file_name):
    log_files = []
    file1 = open(file_name, "r")
    log_files.append(file1.readlines())
    file1.close()
    return log_files

