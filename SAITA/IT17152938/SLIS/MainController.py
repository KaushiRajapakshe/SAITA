from Software import Software
from Osdata import Osdata


class MainController:
    soft = None
    osdata = None

    def __init__(self):
        self.soft = Software()
        self.osdata = Osdata()

    # get complete software data set
    def get_soft_list(self):
        db_soft_list = self.soft.get_all_software()
        installed_list = self.osdata.get_installed_soft_list()
        for app in installed_list:
            for db_app in db_soft_list:
                sp_len = len(app.name.split(db_app['name']))
                if sp_len != 1:
                    print(app.name + "\t" + db_app['name'])
                    print(app.version)
                    db_app['installed'] = 1
                    if not 'installed_ver' in db_app:
                        db_app['installed_ver'] = []
                    db_app['installed_ver'].append(app.version)

        return db_soft_list
