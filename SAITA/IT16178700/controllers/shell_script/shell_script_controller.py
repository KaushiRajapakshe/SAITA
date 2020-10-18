import subprocess
import sys

from SAITA.IT16178700.data import variables


def shell_script_write(script):
    shell_file = open(variables.script_file, "w+")
    shell_file.write(script)
    subprocess.Popen(["powershell.exe", variables.script_file], stdout=sys.stdout)
