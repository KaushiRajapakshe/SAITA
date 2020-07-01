import os
import winapps_change
import platform


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
