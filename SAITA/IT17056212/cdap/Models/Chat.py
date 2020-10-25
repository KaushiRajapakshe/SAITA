class TestChat:
    usrerep = []  # User reply
    sitarep = [["hi"]]  # SAITA reply
    type = None  # type

    def __init__(self):
        self.usrerep = []
        self.sitarep = ["hi"]
        self.mass = 0

    # Get the user reply
    def get_usrerep(self):
        return self.usrerep

    # Set the user reply
    def set_usrerep(self, usrerep):
        self.usrerep.append(usrerep)

    # Get the SAITA reply
    def get_sitarep(self):
        return self.sitarep

    # Set the SAITA reply
    def set_sitarep(self, sitarep):
        self.sitarep.append(sitarep)

    # Get the last user reply
    def get_lastuserreply(self):
        return self.usrerep[len(self.usrerep) - 1]

    # Set the last user reply
    def get_lastsaitareply(self):
        return self.sitarep[len(self.sitarep) - 1]

    # Get type
    def get_type(self):
        return self.type

    # Set type
    def set_type(self, type):
        self.type = type
