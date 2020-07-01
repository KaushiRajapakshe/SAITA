import subprocess
from StopScript import IssuedService

params = [IssuedService]  # POWERSHELL SCRIPT PARAMETERS ( optional )

script_path = "E:\\SLIIT\\4year\\CDAP\\2020-110\\2020-110\\SAITA\\IT17018760\\Powershell\\StopService.ps1"  # POWERSHELL SCRIPT PATH
commandline_options = ["Powershell.exe", '-ExecutionPolicy', 'Unrestricted', script_path]  # INITIALIZING COMMAND
for param in params:  # FOREACH LOOP OF PARAMETERS
    commandline_options.append(param)  # ADDING SCRIPT PARAMETERS TO THE COMMAND

result = subprocess.run(commandline_options, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)  # RUN THE SCRIPT USING SUBPROCESS WITH PARAMS

#print(result.returncode)  # PRINT THE RETURN CODE FROM POWERSHELL SCRIPT
print(result.stdout)  # PRINT THE STANDARD OUTPUT FROM POWERSHELL SCRIPT
print(result.stderr)  # PRINT THE STANDARD ERROR FROM POWERSHELL SCRIPT
