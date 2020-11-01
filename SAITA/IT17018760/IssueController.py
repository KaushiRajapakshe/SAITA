from MainIssueGather import GatherIssue
from ExecuteScripts import Exe

class IssueControl(object):

    ex=None

    #get the issue from the chat controller
    def IssueTakerEmpty(self,issue):
        self.ex=Exe()
        GatherIssue().TakeIssue(issue,self.ex)

        print(self.ex)
        print(issue)
    #execute the next runnable class
    def RunNext(self):

        print(self.ex)
        return self.ex.say_no()
    #if user says yes it terminating from this class call
    def RunDone(self):
        k= self.ex.say_yes()
        self.ex=None
        return k

    def get_input_for_is_sol(self):

        issueget = input("Is your issue solved? ")
        return issueget






