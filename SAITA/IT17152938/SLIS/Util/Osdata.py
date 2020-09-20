import os
from tkinter import filedialog
import tkinter as tk

import winapps_change
import platform
import subprocess
from Data.Log import *
import ctypes as ct

from Gui.GuiPopupWindow import GuiPopupWindow
import zipfile


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

    def search_installed_list_with_ver(self, name, ver):
        install_location = []
        v_no_split = str(ver).split('.')
        v_no_ok = None
        if len(v_no_split) > 1:
            v_no_ok = v_no_split[0] + "." + v_no_split[1]
        else:
            v_no_ok = v_no_split[0] + ".0"
        for app in winapps_change.search_installed(name):
            if app.version is None or app.version == "" or app.install_location is None or app.install_location == "":
                continue
            inst_split = app.version.split('.')
            inst_ok = None
            if len(inst_split) > 1:
                inst_ok = inst_split[0] + "." + inst_split[1]
            else:
                inst_ok = inst_split[0] + ".0"
            if inst_ok == v_no_ok:
                install_location.append(app.install_location)
        return install_location

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
            restore_point[key] = str(result).replace("b'", "").replace("\\r\\n'", "")
        return restore_point

    def get_restorepoint_sequenceNumber(self, point_name):
        code = "Get-ComputerRestorePoint "
        code += "|Where-Object {$_.Description -eq \"" + point_name + "\"} "
        code += "| Select-Object -ExpandProperty SequenceNumber"
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readline()

        return str(result).replace("b'", "").replace("\\r\\n'", "")

    def create_restorepoint(self, point_name, root, acc_ra, work_area):
        sequence_number = self.get_restorepoint_sequenceNumber(point_name)
        if sequence_number == "'":
            return self._create_restorepoint_in(point_name, root, acc_ra, work_area)
        else:
            self.del_restorepoint(point_name)
            return self._create_restorepoint_in(point_name, root, acc_ra, work_area)

    def _create_restorepoint_in(self, point_name, root, acc_ra, work_area):
        massage = GuiPopupWindow(root,
                                 acc_ra,
                                 work_area,
                                 "Wait",
                                 ["Creating Windows Restore Point Please Wait"],
                                 [0.4615, 0.5, 0.2702, 5],
                                 type="wait",
                                 close=False,
                                 )
        massage.top.update()
        massage.top.deiconify()
        code = "Checkpoint-Computer -Description \"" + point_name + "\" -RestorePointType APPLICATION_INSTALL "
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        while process.poll() is None:
            massage.top.update()
        result = process.stdout.readlines()
        massage.top.destroy()
        if not str(result) == "[]":
            add_log(log_types[3], "Osdata", "can't create restore point " + str(result))
            return False
        return True

    def del_restorepoint(self, point_name):
        # first get sequenceNumber for restorepoint using Description
        sequence_number = self.get_restorepoint_sequenceNumber(point_name)
        if str(sequence_number) == "'":
            add_log(log_types[3], "Osdata", "Can't find sequenceNumber for Restore Point Description " + point_name)
            return False
        # call delete ps1
        libc = ct.cdll.Srclient
        if not str(libc.SRRemoveRestorePoint(int(sequence_number))) == "0":
            add_log(log_types[3], "Osdata", "Fail to delete Restore Point")
            return False

        return True

    def get_environment_variable(self, variable_name):
        code = "[Environment]::GetEnvironmentVariable('" + variable_name + "', 'Machine')"
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readline()
        return str(result).replace("b'", "").replace("\\r\\n'", "").replace("\\\\", "\\").split(';')

    def add_environment_variable(self, variable_name, variable):
        var_array = self.get_environment_variable(variable_name)
        new_var = variable + ';'
        for var in var_array:
            new_var += var + ';'
        new_var = new_var.replace(";;", ";")
        code = "[Environment]::SetEnvironmentVariable('" + variable_name + "', '" + new_var + "', 'Machine')"
        process = subprocess.Popen(["powershell",
                                    code],
                                   shell=True, stdout=subprocess.PIPE)
        result = process.stdout.readline()
        if not str(result) == "b''":
            add_log(log_types[3], "Osdata", "can't add environment variable" + str(result))
            return False
        return True

    def search_environment_variable(self, variable_name, variable):
        var_array = self.get_environment_variable(variable_name)
        search = []
        for var in var_array:
            if len(var.lower().split(str(variable).lower())) != 1:
                search.append(var)
        return search

    def run_installer(self, node, root, acc_ra, work_area):
        self.minimize_all()
        me = "Waiting for install " + node.get_soft_name() + " version : " + node.get_ver()
        massage = GuiPopupWindow(root,
                                 acc_ra,
                                 work_area,
                                 "Wait",
                                 [me],
                                 [0.4615, 0.5, 0.2702, 5],
                                 type="wait",
                                 close=False,
                                 )
        massage.top.update()
        massage.top.deiconify()
        filename="";
        if node.get_setup_type() == 1:
            if node.get_exe_param()== None:
                comand = "Start-Process \"" + node.get_file_path() + "\" -wait"
            else:
                comand = "Start-Process \"" + node.get_file_path() + \
                    "\" -argumentlist \""+node.get_exe_param()+"\" -wait"
            process = subprocess.Popen(["powershell", comand], shell=True, stdout=subprocess.PIPE)
            massage.top.deiconify()
            while process.poll() is None:
                massage.top.update()
                # print('waiting')
            massage.top.destroy()
        else:
            filename = None
            massage.top.deiconify()
            askdirectory_title = "Extract folder for " + node.get_soft_name() + " version:" + node.get_ver()
            while filename is None or filename == "":
                filename = filedialog.askdirectory(master=massage.top, title=askdirectory_title, mustexist=tk.TRUE)

            with zipfile.ZipFile(node.get_file_path(), 'r') as zip_ref:
                for member in zip_ref.infolist():
                    zip_ref.extract(member, filename)
                    massage.top.update()
            massage.top.destroy()
        return filename

        # result = process.stdout.readlines()

    def minimize_all(self):
        code = " (New-Object -ComObject Shell.Application).MinimizeAll()"
        process = subprocess.Popen(["powershell", code], shell=True, stdout=subprocess.PIPE)
        process.wait()
