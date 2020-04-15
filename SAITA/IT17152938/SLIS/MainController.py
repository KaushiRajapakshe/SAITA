from Software import Software
from Osdata import Osdata


class MainController:
    soft = None
    osdata = None

    def __init__(self):
        self.soft = Software()
        self.osdata = Osdata()

    def get_soft_list(self):
        db_soft_list = self.soft.get_all_software()
        print(db_soft_list)
