import subprocess

from ARTA.data import variables


# Write Shell Script and
# Execute Shell Script
def shell_script_write(script):
    # Open power shell script file or create power shell script file
    shell_file = open(variables.script_file, "w+")
    # Write KB Error Solution on power shell script file
    s_list = script.split('\\n')
    for s in s_list:
        shell_file.write("\n" + s)

    # Close opened file
    shell_file.close()
    # Execute power shell script solution
    process = subprocess.Popen(["powershell.exe", "powershell -ExecutionPolicy ByPass -File " + variables.script_file],
                               stdout=subprocess.PIPE)
    result = process.stdout.readline()
    return str(result).replace("b'", "").replace("\\r\\n'", "")
