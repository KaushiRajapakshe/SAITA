import os
from tkinter import filedialog,messagebox
import tkinter as tk
from Data.Log import *
from Util.SayText import SayText
from Util.SoftwareTreeCreator import SoftwareTreeCreator
from Util.Software import Software
from Util.Osdata import Osdata
from Data.Veriables import restore_point_name, file_location, download_location, end_text
from Gui.GuiPopupWindow import GuiPopupWindow
import requests
from pathlib import Path


class MainController:
    soft = None
    osdata = None
    install_soft_list = []

    def __init__(self):
        self.install_soft_list = []
        self.soft = Software()
        self.osdata = Osdata()

    # get complete software data set
    def get_soft_list_full(self):
        return self.get_soft_list(self.soft.get_all_software())

    # get serch software data set
    def get_soft_list_search(self, soft):
        return self.get_soft_list(self.soft.get_search_software(soft))

    def get_soft_list(self, db_soft_list):
        self.install_soft_list = []
        installed_list = self.osdata.get_installed_soft_list()
        for app in installed_list:
            for db_app in db_soft_list:
                sp_len = len(app.name.lower().split(str(db_app['name']).lower()))
                if sp_len != 1:
                    db_app['installed'] = 1
                    if not 'installed_ver' in db_app:
                        db_app['installed_ver'] = []
                    db_app['installed_ver'].append(app.version)
        self.create_installed_list(db_soft_list)
        return db_soft_list

    def get_soft_name_by_id(self, soft_id):
        soft_name = self.soft.get_soft_name_by_id(soft_id)
        for soft in soft_name:
            return soft['name']

        add_log(log_types[1], "MainController", "get_soft_name_by_id : " + str(soft_id) + " id not found")
        return ""

    def get_soft_version_by_id(self, soft_ver):
        soft_ver = self.soft.get_soft_ver_by_id(soft_ver)
        for soft in soft_ver:
            return soft['v_no']

        add_log(log_types[1], "MainController", "get_soft_version_by_id : " + str(soft_ver) + " id not found")
        return ""

    def create_installed_list(self, softlist):
        # install_soft_list = []
        for soft in softlist:
            for ver in self.soft.get_all_version(soft['id']):
                if 'installed_ver' in soft:
                    for inst in soft['installed_ver']:
                        if inst is None:
                            continue
                        inst_split = inst.split('.')
                        inst_ok = None
                        v_no_split = str(ver['v_no']).split('.')
                        v_no_ok = None
                        if len(inst_split) > 1:
                            inst_ok = inst_split[0] + "." + inst_split[1]
                        else:
                            inst_ok = inst_split[0] + ".0"

                        if len(v_no_split) > 1:
                            v_no_ok = v_no_split[0] + "." + v_no_split[1]
                        else:
                            v_no_ok = v_no_split[0] + ".0"
                        if inst_ok == v_no_ok:
                            self.install_soft_list.append(ver['id'])

    def get_insalled_list(self):
        return self.install_soft_list

    def create_setup(self, install_list):
        self.get_soft_list_full()
        per_install_softwares = list(dict.fromkeys(self.get_insalled_list()))
        soft_tree = SoftwareTreeCreator()
        tree = soft_tree.create_tree(install_list)
        for node_array in tree:
            for node in node_array:
                try:
                    per_install_softwares.index(node.get_ver_id())
                    node.set_do_install(False)
                except:
                    node.set_do_install(True)
        return tree

    def run_install(self, root, soft_tree, acc_ra, work_area):
        list = []
        self.osdata.create_restorepoint(restore_point_name, root, acc_ra, work_area)
        for soft in soft_tree:
            for node in soft:
                if node.get_do_install() == 1:
                    # if node.get_do_install():
                    #     if not node.get_setup_type() == 1:
                    #         node.set_file_path(os.path.abspath("../Temp/Eclipse_3_7/eclipse.zip"))
                    #         self.osdata.run_installer(node, root, acc_ra, work_area)
                    #         install_soft = self.osdata.search_installed_list_with_ver(node.get_soft_name(), node.get_ver())
                    #         print(install_soft)
                    #         continue
                    #     if node.get_soft_name()=="Java":
                    #         node.set_file_path(os.path.abspath("../Temp/Java_8/jdk.exe"))
                    #         self.osdata.run_installer(node, root, acc_ra, work_area)
                    #         install_soft = self.osdata.search_installed_list_with_ver(node.get_soft_name(), node.get_ver())
                    #         print(install_soft)
                    #         continue

                    download_link = file_location + node.setup_link
                    message = node.get_soft_name() + " Version:" + node.get_ver() + " Downloading ...."
                    massage = GuiPopupWindow(root,
                                             acc_ra,
                                             work_area,
                                             "Downloading",
                                             [message],
                                             [0.4615, 0.25, 0.2702, 5],
                                             type="download",
                                             close=False,
                                             )
                    massage.top.deiconify()
                    url_split = download_link.split("/")
                    file_name = url_split[len(url_split) - 1]

                    req = requests.get(download_link, stream=True)
                    massage.progress["value"] = 0
                    maxbytes = int(req.headers['content-length'])
                    massage.progress["maximum"] = maxbytes
                    chunk_size = 1024
                    dl_size = 0
                    c_path = download_location + node.get_soft_name() + "_" + node.get_ver().replace(".", "_")
                    Path(c_path).mkdir(parents=True, exist_ok=True)
                    file_path = c_path + "/" + file_name
                    with open(file_path, "wb") as f:
                        for data in req.iter_content(chunk_size=chunk_size):
                            dl_size += len(data)
                            done = round((100 * dl_size / maxbytes), 1)
                            massage.progress["value"] = round(dl_size)
                            massage.progress_num.config(text=str(done) + " %")
                            massage.top.update()
                            f.write(data)
                        f.close()
                    # list.append(file_path)
                    # print(file_path)
                    massage.top.destroy()
                    # node.print_node()
                    # start install
                    node.set_file_path(os.path.abspath(file_path))
                    filename = self.osdata.run_installer(node, root, acc_ra, work_area)

                    #start path set process
                    path_list = self.soft.get_path(node.get_ver_id())
                    filename = None
                    if len(path_list) > 0:
                        if node.get_exe_param() == None:
                            SayText.get_say_text().say(
                                "Select " + node.get_soft_name() + " version " + node.get_ver()+" installed location")
                            while filename is None or filename == "":
                                filename = filedialog.askdirectory(master=root, title="select "+node.get_soft_name()+" installed directory",
                                                           mustexist=tk.TRUE)

                        for path in path_list:
                            full_env_path=None
                            if file_name == None:
                                full_env_path = path['var_path']
                            else:
                                full_env_path = os.path.join(filename,path['var_path'])
                                full_env_path = full_env_path.replace('/','\\')
                            exsisting_v=self.osdata.search_environment_variable(path['var_name'],node.get_soft_name())
                            if len(exsisting_v) > 0:
                                txt='Existing environment variable found for '+node.get_soft_name()+' : '+path['var_name']
                                txt+='\n its\'  located to:\n'
                                for exet in exsisting_v:
                                    txt += '\t'+exet+'\n'
                                txt += 'Is it ok to overwrite?'
                                MsgBox = messagebox.askquestion('Existing environment variable found',
                                                                   txt,
                                                                   icon='warning', master=root)

                                if not MsgBox == 'yes':
                                    continue

                            self.osdata.add_environment_variable(path['var_name'], full_env_path,root, acc_ra, work_area, node.get_soft_name())


                    # root.deiconify()
        messagebox.showinfo("Completed", 'software installation completed with dependencies ', master=root)
        root.destroy()