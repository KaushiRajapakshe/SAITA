import csv

from Models.Chat import TestChat
from Controllers.Chat_process_controller import mainController
from Data import Questions
from Data.Variables import *


class ChatController:
    next_q = []
    chat = None
    net_ident_ques = Questions.network_identifying_questions
    net_cat_ques = Questions.network_categorizing_questions
    net_ident_ques.pop(len(net_ident_ques) - 1)
    net_cat_ques.pop(len(net_cat_ques) - 1)
    direct_ident_ques = Questions.directory_identifying_questions
    direct_cat_ques = Questions.directory_categorizing_questions
    direct_ident_ques.pop(len(direct_ident_ques) - 1)
    direct_cat_ques.pop(len(direct_cat_ques) - 1)
    userconf_ident_ques = Questions.userconf_identifying_questions
    userconf_cat_ques = Questions.userconf_categorizing_questions
    userconf_ident_ques.pop(len(userconf_ident_ques) - 1)
    userconf_cat_ques.pop(len(userconf_cat_ques) - 1)
    network_q = net_ident_ques + net_cat_ques
    directory_q = direct_ident_ques + direct_cat_ques
    user_q = userconf_ident_ques + userconf_cat_ques

    def __init__(self):
        self.chat = TestChat()
        self.maincon = mainController()

    def chat_question_sequence(self, acc_ra, work_area, win_root):
        ch = True

        if self.chat.get_isrun() is not None:
            self.chat.set_isrun(None)
            self.chat.set_rate(self.chat.get_lastuserreply())
            self.chat.set_sitarep("Thank you for feedback of: " + str(self.chat.get_rate()))
            if 5 >= int(self.chat.get_rate()) >= 1:
                with open(rank_log_csv, newline='') as f1:
                    reader = csv.reader(f1)
                    row1 = next(reader)
                f1.close()
                print(row1)

                w, x, y, z = row1[0], row1[1], row1[2], int(self.chat.get_rate())
                csvRow = [w, x, y, z]
                csvfile = issue_history_csv
                with open(csvfile, "a", newline='') as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(csvRow)
                fp.close()

                f3 = open(rank_log_csv, "w")
                f3.truncate()
                f3.close()
                win_root.destroy()
            return

        for cat_in in network_synonyms:
            if cat_in in self.chat.get_lastuserreply().lower() and self.chat.get_type() is None:
                self.chat.set_type('network')
                self.chat.set_sitarep(self.network_q[0])
                ch = False
                break
            else:
                for cat_in2 in directory_synonyms:
                    if cat_in2 in self.chat.get_lastuserreply().lower() and self.chat.get_type() is None:
                        self.chat.set_type('directory')
                        self.chat.set_sitarep(self.directory_q[0])
                        ch = False
                        break
                    else:
                        for cat_in3 in userconf_synonyms:
                            if cat_in3 in self.chat.get_lastuserreply().lower() and self.chat.get_type() is None:
                                self.chat.set_type('user')
                                self.chat.set_sitarep(self.user_q[0])
                                ch = False
                                break
                            elif self.chat.get_type() is None:
                                self.chat.set_sitarep("Please enter the issue category as (network/ directory/ user "
                                                      "configuration issue) ")
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
                # ranking question
                self.chat.set_isrun("run")
                val = self.maincon.process(acc_ra, work_area, win_root) + "\n\n" + Questions.Ranking_question
                self.chat.set_sitarep(val)
                # ----------


        elif self.chat.get_type() == 'directory' and ch:
            lastsaitareply = self.directory_q.index(self.chat.get_lastsaitareply())
            if not lastsaitareply == len(self.directory_q) - 1:
                self.chat.set_sitarep(self.directory_q[lastsaitareply + 1])
            else:

                self.chat.set_type(None)

                user_reply_array = self.chat.get_usrerep()
                user_reply_array.reverse()
                send_array = []
                for k in range(len(self.directory_q) + 1):
                    send_array.append(user_reply_array[k])
                send_array.reverse()
                self.maincon.set_input(send_array)
                # ranking question
                self.chat.set_isrun("run")
                val = self.maincon.process(acc_ra, work_area, win_root) + "\n\n" + Questions.Ranking_question
                self.chat.set_sitarep(val)
                # ----------

        elif self.chat.get_type() == 'user' and ch:
            lastsaitareply = self.user_q.index(self.chat.get_lastsaitareply())
            if not lastsaitareply == len(self.user_q) - 1:
                self.chat.set_sitarep(self.user_q[lastsaitareply + 1])
            else:

                self.chat.set_type(None)

                user_reply_array = self.chat.get_usrerep()
                user_reply_array.reverse()
                send_array = []
                for k in range(len(self.user_q) + 1):
                    send_array.append(user_reply_array[k])
                send_array.reverse()
                self.maincon.set_input(send_array)
                self.chat.set_sitarep(self.maincon.process(acc_ra, work_area, win_root))
                # ranking question
                self.chat.set_isrun("run")
                val = self.maincon.process(acc_ra, work_area, win_root) + "\n\n" + Questions.Ranking_question
                self.chat.set_sitarep(val)
                # ----------

    def get_chat(self):
        return self.chat
