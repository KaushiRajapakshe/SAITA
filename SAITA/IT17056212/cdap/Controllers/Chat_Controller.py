from Models.Chat import TestChat
from Controllers.Chat_process_controller import mainController
from Data import Questions


class ChatController:
    next_q = []
    chat = None
    net_ident_ques = Questions.network_identifying_questions
    net_cat_ques = Questions.network_categorizing_questions
    net_ident_ques.pop(len(net_ident_ques) - 1)
    net_cat_ques.pop(len(net_cat_ques) - 1)
    network_q = net_ident_ques + net_cat_ques

    def __init__(self):
        self.chat = TestChat()
        self.maincon = mainController()

    def chat_question_sequence(self):
        ch = True
        if self.chat.get_lastuserreply() == 'network' and self.chat.get_type() is None:
            self.chat.set_type('network')
            self.chat.set_sitarep(self.network_q[0])
            ch = False
        elif self.chat.get_type() is None:
            self.chat.set_sitarep("Please enter type")
            ch = False

        if self.chat.get_type() == 'network' and ch:
            lastsaitareply = self.network_q.index(self.chat.get_lastsaitareply())
            if not lastsaitareply == len(self.network_q) - 1:
                self.chat.set_sitarep(self.network_q[lastsaitareply + 1])
            else:

                self.chat.set_type(None)

                user_reply_array = self.chat.get_usrerep()
                user_reply_array.reverse()
                send_array = []
                for k in range(len(self.network_q) + 1):
                    send_array.append(user_reply_array[k])
                send_array.reverse()
                self.maincon.set_input(send_array)
                self.chat.set_sitarep(self.maincon.process())

    def get_chat(self):
        return self.chat
