# SAITA Pre selected Application related issue solving Agent
# Chat Model class

class TestChat:
    usrerep = []
    sitarep = [["hi"]]
    loop = 0

    def __init__(self):
        self.usrerep = []  # User reply for SAITA variable
        self.sitarep = ["hi"]  # SAITA reply for user variable
        self.loop = 0  # Loop for identify pre selected question category variable

    # getter method user reply
    def get_usrerep(self):
        return self.usrerep

    # setter method user reply
    def set_usrerep(self, usrerep):
        self.usrerep.append(usrerep)

    # getter method saita reply
    def get_sitarep(self):
        return self.sitarep

    # setter method saita reply
    def set_sitarep(self, sitarep):
        self.sitarep.append(sitarep)

    # getter method last user reply
    def get_lastuserreply(self):
        return self.usrerep[len(self.usrerep) - 1]

    # getter method check user reply
    def get_check_userreply(self):
        return self.usrerep[len(self.usrerep) - 2]

    # getter method saita last reply
    def get_lastsaitareply(self):
        return self.sitarep[len(self.sitarep) - 1]

    # getter method loop
    def get_loop(self):
        return self.loop

    # setter method loop
    def set_loop(self, loop):
        self.loop = loop
