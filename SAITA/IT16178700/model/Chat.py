class TestChat:
    usrerep = []
    sitarep = [["hi"]]
    loop = 0

    def __init__(self):
        self.usrerep = []
        self.sitarep = ["hi"]
        self.mass = 0
        self.loop = 0

    def get_usrerep(self):
        return self.usrerep

    def set_usrerep(self, usrerep):
        self.usrerep.append(usrerep)

    def get_sitarep(self):
        return self.sitarep

    def set_sitarep(self, sitarep):
        self.sitarep.append(sitarep)

    def get_lastuserreply(self):

        return self.usrerep[len(self.usrerep)-1]

    def get_check_userreply(self):
        return self.usrerep[len(self.usrerep)-2]

    def get_lastsaitareply(self):
        return self.sitarep[len(self.sitarep)-1]

    def get_loop(self):
        return self.loop

    def set_loop(self, loop):
        self.loop = loop
