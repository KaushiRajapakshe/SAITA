from SAITA.IT16178700.model.Chat import TestChat


class ChatController:
    next_q = []
    chat = None
    application_q = ['Please enter version of your application.?',
                     'Please enter your error discretion.?',
                     'Please wait until error analyzing',
                     'Insight-dashboard.jar service run on 8080 port.',
                     ' Do you need to continue.?',
                     'Your problem is solved.']

    def __init__(self):
        self.chat = TestChat()

    def chat_question_sequence(self):
        ch = True
        if (
                self.chat.get_lastuserreply() == 'Apache' or self.chat.get_lastuserreply() == 'Xampp') and self.chat.get_type() is None:
            self.chat.set_type('Apache')
            self.chat.set_sitarep(self.application_q[0])
            ch = False
        elif self.chat.get_type() is None:
            self.chat.set_sitarep("Please enter your application name.?")
            ch = False

        if (self.chat.get_type() == 'Apache' or self.chat.get_lastuserreply() == 'Xampp') and ch:
            last_saita_reply = self.application_q.index(self.chat.get_lastsaitareply())
            if not last_saita_reply == len(self.application_q) - 1:
                self.chat.set_sitarep(self.application_q[last_saita_reply + 1])
            else:

                self.chat.set_type(None)

                user_reply_array = self.chat.get_usrerep()
                user_reply_array.reverse()
                send_array = []
                for k in range(len(self.application_q) + 1):
                    send_array.append(user_reply_array[k])
                send_array.reverse()
                self.maincon.set_input(send_array)
                self.chat.set_sitarep(self.maincon.process())

    def get_chat(self):
        return self.chat
