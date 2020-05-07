import os
import winapps_change


class Osdata:

    # get installed software list
    def get_installed_soft_list(self):
        return winapps_change.list_installed()

    # search in installed list
    def search_installed_list(self, name):
        [app] = winapps_change.search_installed(name)
        return app