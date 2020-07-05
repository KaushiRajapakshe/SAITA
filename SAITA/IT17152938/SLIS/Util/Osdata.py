import os
import winapps_change
import platform
import subprocess
from Data.Veriables import powershellcode_floder_location
from Data.Log import *


class Osdata:

    # get installed software list
    def get_installed_soft_list(self):
        # for app in winapps_change.list_installed():
        #     print(app.name, app.install_location, app.version)
        return winapps_change.list_installed()

    # search in installed list
    def search_installed_list(self, name):
        [app] = winapps_change.search_installed(name)
        return app

    def get_os_architecture_type(self):
        return platform.architecture()[0]

    def get_restorepoint(self, point_name):
        # Where{ $_.ConvertToDateTime($_.CreationTime) -lt  $removeDate} |
        keys = ["CreationTime", "Description", "SequenceNumber", "EventType", "RestorePointType"]
        restore_point = {}
        for key in keys:
            code = "Get-ComputerRestorePoint "
            code += "|Where-Object {$_.Description -eq \"" + point_name + "\"} "
            code += "| Select-Object -ExpandProperty " + key
            process = subprocess.Popen(["powershell",
                                        code],
                                       shell=True, stdout=subprocess.PIPE)
            result = process.stdout.readline()
            line = str(result).replace("b'", "")
            line = line.replace("\\r\\n'", "")
            restore_point[key] = line
        return restore_point

    def get_restorepoint_sequenceNumber(self,point_name):
        code = "Get-ComputerRestorePoint "
        code += "|Where-Object {$_.Description -eq \"" + point_name + "\"} "
        code += "| Select-Object -ExpandProperty SequenceNumber"
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readline()

        line = str(result).replace("b'", "")
        return line.replace("\\r\\n'", "")

    def create_restorepoint(self, point_name):
        sequence_number = self.get_restorepoint_sequenceNumber(point_name)
        if sequence_number == "'":
            return self._create_restorepoint_in(point_name)
        else:
            self.del_restorepoint(point_name)
            return self._create_restorepoint_in(point_name)

    def _create_restorepoint_in(self,point_name):
        code = "Checkpoint-Computer -Description \"" + point_name + "\" -RestorePointType APPLICATION_INSTALL "
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readlines()
        if not str(result) == "[]":
            add_log(log_types[3], "Osdata", "can't create restore point " + str(result))
            return False
        return True

    def del_restorepoint(self, point_name):
        # first get sequenceNumber for restorepoint using Description
        sequence_number = self.get_restorepoint_sequenceNumber(point_name)
        if str(sequence_number) == "'":
            add_log(log_types[3], "Osdata", "Can't find sequenceNumber for Restore Point Description "+point_name)
            return False
        # call delete ps1
        code = "powershell -ExecutionPolicy ByPass -File  " \
               + powershellcode_floder_location + \
               "Delete-RestorePoint.ps1 " + \
               sequence_number
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readline()
        if not str(result) == "b'0\\r\\n'":
            add_log(log_types[3], "Osdata", "Fail to delete Restore Point")
            return False

        return True
