import subprocess
import time

from Models.Chat import TestChat
from tkinter.constants import END
from IssueController import IssueControl
from Data.Variables import *


class ChatController:
    next_q = []
    chat = None

    chatch = True;

    def __init__(self):
        self.chat = TestChat()
        self.maincon = IssueControl()

    def chat_do(self, chat_log):
        if self.chatch:
            self.chatch = False

            # logsize=os.path.getsize("log_file.txt")
            # print(logsize)

            self.maincon.IssueTakerEmpty(self.chat.get_lastuserreply())
            # print(self.chat.get_lastuserreply())
            time.sleep(5)
            self.chat.set_sitarep("Is your issue solved in this moment? (yes/no)");
        else:
            # print(self.chat.get_lastuserreply())
            if (self.chat.get_lastuserreply() == 'yes'):
                self.chatch = True
                self.chat.set_sitarep(self.maincon.RunDone());
                self.chat.set_sitarep("Your issue solved.Thank you for join with SAITA. ");
                process = subprocess.Popen(["powershell", restartCode], shell=True, stdout=subprocess.PIPE)
            elif self.chat.get_lastuserreply() == 'no':
                self.maincon.RunNext();
                time.sleep(5)
                self.chat.set_sitarep("Is your issue solved in this moment? (yes/no)");
            else:
                self.chat.set_sitarep("Please Send Correct Feedback. Is your issue solved in this moment? (yes/no)");

        chat_log.ChatLog.insert(END, "SAITA : " + self.chat.get_lastsaitareply() + '\n\n')

    def get_chat(self):
        return self.chat

    def set_chat_log(self, ch):
        self.chat_log = ch
