import csv

from Controllers.Decisiontree_controller import DecisiontreeController
from Controllers.Query import Queries
from Controllers.Sentence_Controller import SentenceController
from Data.Variables import *
from Models.Inputs import Input
from Controllers.Ranking_controller import RankingController
from Util.ScriptGenerator import ScriptGenerator


class mainController:
    inp = None
    input = []

    def __init__(self):
        self.input = []
        self.inp = Input.get_input()

    def set_input(self, userreply):
        self.input = userreply

    def process(self, acc_ra, work_area, win_root):
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
                    else:
                        for cat_in3 in userconf_synonyms:
                            if cat_in3 in self.input[0].lower():
                                category = 'user'
                                break

        self.inp.set_category(category)

        component = 'identifying'
        self.inp.set_component(component)

        if self.inp.get_component() == 'identifying':
            if self.inp.get_category() == 'network':
                self.inp.set_error_msg(self.input[1])
                self.inp.set_error_code(self.input[2])
                self.inp.set_type(self.input[3])

            elif self.inp.get_category() == 'directory':
                self.inp.set_error_msg(self.input[1])
                self.inp.set_error_code(self.input[2])
                self.inp.set_type(self.input[3])
                self.inp.set_path_para(self.input[4])

            elif self.inp.get_category() == 'user':
                self.inp.set_error_msg(self.input[1])
                self.inp.set_error_code(self.input[2])
                self.inp.set_type(self.input[3])
                self.inp.set_name_para(self.input[4])

        predicted_issue_ids = DecisiontreeController.decisontree_results(self.inp.get_component(),
                                                                         self.inp.get_category(),
                                                                         self.inp.get_input_array())

        # send issue list for ranking
        rank = RankingController()
        issue_id = rank.process_decisiontree_result(predicted_issue_ids)
        print(issue_id)

        # create tempory ranking info on rank_log.csv
        cat = self.inp.get_category()
        typ = self.inp.get_type()

        itype_rank = None
        category_rank = None
        if cat == 'network':
            category_rank = 1
            if typ == 'intranet':
                itype_rank = 1
            elif typ == 'internet':
                itype_rank = 2
        elif cat == 'directory':
            category_rank = 2
            if typ == 'file':
                itype_rank = 3
            elif typ == 'directory':
                itype_rank = 4
            elif typ == 'drive':
                itype_rank = 5
        elif cat == 'user':
            category_rank = 3
            if typ == 'local':
                itype_rank = 6

        w, x, y = category_rank, itype_rank, issue_id
        csvRow = [w, x, y]
        csvfile = rank_log_csv
        with open(csvfile, "a", newline='') as fp1:
            wr = csv.writer(fp1, dialect='excel')
            wr.writerow(csvRow)
        fp1.close()

        component = 'categorizing'
        self.inp.set_component(component)

        if self.inp.get_component() == 'categorizing':
            if self.inp.get_category() == 'network':
                self.inp.set_question1(self.input[4])
                self.inp.set_question2(self.input[5])
                self.inp.set_question3(self.input[6])
                self.inp.set_question4(self.input[7])

            elif self.inp.get_category() == 'directory':
                self.inp.set_question1(self.input[5])
                self.inp.set_question2(self.input[6])
                self.inp.set_question3(self.input[7])
                self.inp.set_question4(self.input[8])

            elif self.inp.get_category() == 'user':
                self.inp.set_question1(self.input[5])
                self.inp.set_question2(self.input[6])
                self.inp.set_question3(self.input[7])
                self.inp.set_question4(self.input[8])

        predicted_solution_type = DecisiontreeController.decisontree_results(self.inp.get_component(),
                                                                             self.inp.get_category(),
                                                                             self.inp.get_input_array())
        solution_id = None
        for key2 in predicted_solution_type.keys():
            print(key2)
            solution_type = key2
            if solution_type == "non-tech":
                solution_id = Queries.get_nontech_solution_id_by_issue_id(issue_id)

                print(solution_id[0][0])
                nontech_keyward = Queries.get_keywards_by_nontech_solution_id(solution_id[0][0])
                print(nontech_keyward)
                sentence = SentenceController.sentence_generator_results(nontech_keyward)
                print("Main Output: " + sentence)
                return sentence
            elif solution_type == "tech":
                solution_id = Queries.get_tech_solution_id_by_issue_id(issue_id)
                permant_para = Queries.get_permenant_parameter_by_issue_id(issue_id)
                if permant_para[0][0] != 'None':
                    print(permant_para[0][0])
                    self.inp.set_name_para(permant_para[0][0])
                else:
                    print(solution_id[0][0])
                y = ScriptGenerator()

                return y.process_sequence(solution_id[0][0], acc_ra, work_area, win_root)
