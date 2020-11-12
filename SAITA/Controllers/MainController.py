import os
import subprocess
from random import randrange
from Data.Variables import *
from difflib import SequenceMatcher


class MainController:

    def open_program(self, user_input, root):
        cata = self.find_cata(user_input)
        if cata ==5:
            return True
        else:
            self.run_program(cata, root)
            return False

    def find_cata(self, input):

        a = 'Application related issue'
        b = 'Windows service related issue or missing dll issue'
        c = 'Fundamental(basic) Windows issues'
        d = 'Installation install Software list and Environment Setup'

        if input == '1':
            return 0
        elif input == '2':
            return 1
        elif input == '3':
            return 2
        elif input == '4':
            return 3
        else:
            ratio = SequenceMatcher(None, a.lower(), input.lower()).ratio()
            ratio1 = SequenceMatcher(None, b.lower(), input.lower()).ratio()
            ratio2 = SequenceMatcher(None, c.lower(), input.lower()).ratio()
            ratio3 = SequenceMatcher(None, d.lower(), input.lower()).ratio()
            print('ratio: '+str(ratio))
            print('ratio1: ' + str(ratio1))
            print('ratio2: ' + str(ratio2))
            print('ratio3: ' + str(ratio3))
            if ratio > 0.6:
                return 0
            elif ratio1 > 0.56:
                return 1
            elif ratio2 > 0.6:
                return 2
            elif ratio3 > 0.6:
                return 3
            else:
                return 5

    def run_program(self, scriptid, root):
        root.withdraw()
        code = "Start-Process -WindowStyle hidden -Wait -FilePath '" + os.path.abspath(bat_files[scriptid]) + "'"
        print(code)
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readline()
        root.deiconify()
