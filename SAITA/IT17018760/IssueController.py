from MainIssueGather import GatherIssue
from ExecuteScripts import Exe

class IssueControl(object):

    ex=None


    def IssueTakerEmpty(self,issue):
        self.ex=Exe()
        GatherIssue().TakeIssue(issue,self.ex)

        print(self.ex)
        print(issue)

    def RunNext(self):

        print(self.ex)
        return self.ex.say_no()

    def RunDone(self):
        k= self.ex.say_yes()
        self.ex=None
        return k

    def get_input_for_is_sol(self):

        issueget = input("Is your issue solved? ")
        return issueget






