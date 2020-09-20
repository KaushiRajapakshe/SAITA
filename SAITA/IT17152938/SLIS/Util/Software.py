from Util.DBConnection import DBConnection


class Software:
    db = None

    @classmethod
    def __init__(self):
        self.db = DBConnection()

# get all software list from db
    @classmethod
    def get_all_software(cls):
        return cls.db.execute_query('Select * from software where del=%s order by id', ('0',))

# get search software list from db
    @classmethod
    def get_search_software(cls, soft):
        soft_ser='%'+soft+'%'
        return cls.db.execute_query('Select * from software where LOWER(`name`) LIKE %s and del=%s', (soft_ser, '0'))

# get all software version list from db
    @classmethod
    def get_all_version(cls, soft_id):
        return cls.db.execute_query('Select * from version where del=%s and soft_id=%s order by id desc', ('0', str(soft_id)))

# get all dependency list for version from db
    @classmethod
    def get_dependency(cls, ver_id):
        return cls.db.execute_query('Select depend_soft_id from dependency where del=%s and v_id=%s', ('0', ver_id))

# get all path list for version from db
    @classmethod
    def get_path(cls, ver_id):
        return cls.db.execute_query('Select * from e_veriables where del=%s and v_id=%s', ('0', ver_id))


# get software name using software id
    @classmethod
    def get_soft_name_by_id(cls, soft_id):
        return cls.db.execute_query('Select `name` from software where del=%s and id=%s', ('0', str(soft_id)))

# get software version number using version id
    @classmethod
    def get_soft_ver_by_id(cls, ver_id):
        return cls.db.execute_query('Select v_no from version where del=%s and id=%s', ('0', str(ver_id)))

# get software version data using version id
    @classmethod
    def get_soft_ver_data_by_id(cls, ver_id):
        return cls.db.execute_query('Select * from version where del=%s and id=%s', ('0', str(ver_id)))
