from Models.Chat import Chat
from Controllers.MainController import MainController


class ChatController:
    chat = None
    main = None

    def __init__(self):
        self.chat = Chat()
        self.main = MainController()

    def process_user_input(self, root):
        ret = self.main.open_program(self.chat.get_lastuserreply(), root)
        print(ret)
        if ret == True:
            self.chat.set_sitarep(
                "Your troubleshooting category cannot be identified. Please repeat the issue briefly.")
        else:
            self.chat.set_sitarep("Thank you for using SAITA. Please enter an another issue to continue...")

    def get_chat(self):
        return self.chat
