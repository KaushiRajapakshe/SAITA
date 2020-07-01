import subprocess
import sys

p = subprocess.Popen(["powershell.exe",
                      "D:\\testShellScript.ps1"],
                     stdout=sys.stdout)
p.communicate()


