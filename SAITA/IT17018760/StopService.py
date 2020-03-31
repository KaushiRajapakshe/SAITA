import sys
import subprocess

from StartService import commandline_options

params = ['EventSystem']  # POWERSHELL SCRIPT PARAMETERS ( optional )
def main():
    cmd = ["PowerShell", "-ExecutionPolicy", "Unrestricted", "-File", ".\\StopService.ps1"]  # Specify relative or absolute path to the script
    ec = subprocess.call(cmd)
    print("Powershell returned: {0:d}".format(ec))
for param in params:  # FOREACH LOOP OF PARAMETERS
    commandline_options.append(param)  # ADDING SCRIPT PARAMETERS TO THE COMMAND

result = subprocess.run(commandline_options, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)  # RUN THE SCRIPT USING SUBPROCESS WITH PARAMS


if __name__ == "__main__":
    print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    main()
    print("\nDone.")