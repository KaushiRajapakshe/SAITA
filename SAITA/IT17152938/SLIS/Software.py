from DBConnection import DBConnection


class Software:
    db = None

    @classmethod
    def __init__(self):
        self.db = db = DBConnection()

# get all software list from db
    @classmethod
    def get_all_software(cls):
        return cls.db.execute_query('Select * from Software where del=%s', ('0',))

# get all software version list from db
    @classmethod
    def get_all_version(cls, soft_id):
        return cls.db.execute_query('Select * from version where del=%s and softId=$s', ('0', soft_id))

# get all dependency list for version from db
    @classmethod
    def get_dependency(cls, ver_id):
        return cls.db.execute_query('Select * from dependency where del=%s and verId=$s', ('0', ver_id))

# get all path list for version from db
    @classmethod
    def get_path(cls, ver_id):
        return cls.db.execute_query('Select * from path where del=%s and verId=$s', ('0', ver_id))

# get all path list for version from db
    @classmethod
    def get_install_step(cls, ver_id):
        return cls.db.execute_query('Select * from path where del=%s and verId=$s', ('0', ver_id))