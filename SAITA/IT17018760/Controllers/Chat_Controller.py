import subprocess
import time
from SayText import SayText

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
            self.maincon.IssueTakerEmpty(self.chat.get_lastuserreply())
            #waiting to take next SAITA reply to GUI
            time.sleep(5)
            #Calling saytext class to ask issue is solved or not
            SayText.get_say_text().say(issue_solved)
            self.chat.set_sitarep("Is your issue solved in this moment? (yes/no)");
        else:
            #if user reply is yes terminate the system
            if (self.chat.get_lastuserreply() == 'yes'):
                self.chatch = True
                self.chat.set_sitarep(self.maincon.RunDone());
                self.chat.set_sitarep("Your issue solved.Thank you for join with SAITA. ");
                # Calling saytext class to ask restart machine
                SayText.get_say_text().say(if_yes_solved)
                #execute powershell code to restart the machine
                process = subprocess.Popen(["powershell", restartCode], shell=True, stdout=subprocess.PIPE)
            elif self.chat.get_lastuserreply() == 'no':  #if user reply is no execute another optimal path
                self.maincon.RunNext();
                #system wait 5 seconds to get the next users reply
                time.sleep(5)
                self.chat.set_sitarep("Is your issue solved in this moment? (yes/no)");
                # Calling saytext class to ask issue is solved or not
                SayText.get_say_text().say(issue_solved)
            else:
                #if user input the value which is not same as yes or no display this message to the GUI
                self.chat.set_sitarep("Please Send Correct Feedback. Is your issue solved in this moment? (yes/no)");
                #calling say text class to say user entered wrong input
                SayText.get_say_text().say(wrong_input)
        #pass the reply to the Service_GUI and display
        chat_log.ChatLog.insert(END, "SAITA : " + self.chat.get_lastsaitareply() + '\n\n')

    def get_chat(self):
        return self.chat

    def set_chat_log(self, ch):
        self.chat_log = ch
