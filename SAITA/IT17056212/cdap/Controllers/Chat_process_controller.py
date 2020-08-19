from Controllers.Decisiontree_controller import DecisiontreeController
from Controllers.Query import Queries
from Controllers.Sentence_Controller import SentenceController
from Data.Variables import *
from Models.Inputs import Input


class mainController:
    inp = None
    input = []

    def __init__(self):
        self.input = []
        self.inp = Input.get_input()

    def set_input(self, userreply):
        self.input = userreply

    def process(self):
        print(self.input)

        for cat_in in network_synonyms:
            if cat_in in self.input[0].lower():
                category = 'network'
                break
            else:
                for cat_in2 in directory_synonyms:
                    if cat_in2 in self.input[0].lower():
                        category = 'directory'
                        break

        self.inp.set_category(category)

        component = 'identifying'
        self.inp.set_component(component)

        if self.inp.get_component() == 'identifying':
            if self.inp.get_category() == 'network':
                self.inp.set_error_msg(self.input[1])
                self.inp.set_error_code(self.input[2])
                self.inp.set_type(self.input[3])

        predicted_issue_ids = DecisiontreeController.decisontree_results(self.inp.get_component(),
                                                                         self.inp.get_category(),
                                                                         self.inp.get_input_array())
        component = 'categorizing'
        self.inp.set_component(component)

        if self.inp.get_component() == 'categorizing':
            if self.inp.get_category() == 'network':
                self.inp.set_question1(self.input[4])
                self.inp.set_question2(self.input[5])
                self.inp.set_question3(self.input[6])
                self.inp.set_question4(self.input[7])

        predicted_solution_type = DecisiontreeController.decisontree_results(self.inp.get_component(),
                                                                             self.inp.get_category(),
                                                                             self.inp.get_input_array())
        solution_id = None
        for key in predicted_issue_ids.keys():
            print(key)
            issue_id = key
            for key2 in predicted_solution_type.keys():
                print(key2)
                solution_type = key2
                if solution_type == "non-tech":
                    solution_id = Queries.get_nontech_solution_id_by_issue_id(issue_id)

                    print(solution_id[0][0])
                    nontech_keyward = Queries.get_keywards_by_nontech_solution_id(solution_id[0][0])
                    sentence = SentenceController.sentence_generator_results(nontech_keyward)
                    print("Main Output: " + sentence)

                elif solution_type == "tech":
                    solution_id = Queries.get_tech_solution_id_by_issue_id(issue_id)
                    print(solution_id[0][0])
        return sentence
