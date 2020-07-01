import os
import winapps_change
import platform
import subprocess


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
        keys = ["CreationTime", "Description", "SequenceNumber", "EventType", "RestorePointType"]
        restore_point = {}
        for key in keys:
            code = "Get-ComputerRestorePoint "
            code += "|Where-Object {$_.Description -eq \""+point_name+"\"} "
            code += "| Select-Object -ExpandProperty "+key
            print(code)
            process = subprocess.Popen(["powershell",
                                        code],
                                       shell=True, stdout=subprocess.PIPE)
            result = process.stdout.readline()
            line = str(result).replace("b'", "")
            line = line.replace("\\r\\n'", "")
            restore_point[key] = line
        return restore_point
    
