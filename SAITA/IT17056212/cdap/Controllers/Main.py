import csv

from Controllers.Ranking_controller import RankingController
from Data import Questions
from Models.Inputs import Input
from Controllers.Decisiontree_controller import DecisiontreeController
from Controllers.Query import Queries
from Controllers.Sentence_Controller import SentenceController
from Data.Variables import *
from Util.ScriptGenerator import ScriptGenerator

inp = Input.get_input()

if __name__ == '__main__':

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

    with open(rank_log_csv) as f2:
        check_emp = f2.readline()
        if check_emp == '':
            print('Empty rank_log')

            # for x in range(6):
            category_input = input("What type of issue do you have(network/file and directory/User configuration)? ")
            for cat_in in network_synonyms:
                if cat_in in category_input.lower():
                    category = 'network'
                    break
                else:
                    for cat_in2 in directory_synonyms:
                        if cat_in2 in category_input.lower():
                            category = 'directory'
                            break
                        else:
                            for cat_in3 in userconf_synonyms:
                                if cat_in3 in category_input.lower():
                                    category = 'user'
                                    break

            inp.set_category(category)

            component = 'identifying'
            inp.set_component(component)

            if inp.get_component() == 'identifying':
                if inp.get_category() == 'network':
                    msg = input(net_ident_ques[0])
                    inp.set_error_msg(msg)

                    code = input(net_ident_ques[1])
                    inp.set_error_code(code)

                    type = input(net_ident_ques[2])
                    inp.set_type(type)

                elif inp.get_category() == 'directory':
                    msg = input(direct_ident_ques[0])
                    inp.set_error_msg(msg)

                    code = input(direct_ident_ques[1])
                    inp.set_error_code(code)

                    type = input(direct_ident_ques[2])
                    inp.set_type(type)

                    path_par = input(direct_ident_ques[3])
                    inp.set_path_para(path_par)

                elif inp.get_category() == 'user':
                    msg = input(userconf_ident_ques[0])
                    inp.set_error_msg(msg)

                    code = input(userconf_ident_ques[1])
                    inp.set_error_code(code)

                    type = input(userconf_ident_ques[2])
                    inp.set_type(type)

                    usr_name = input(userconf_ident_ques[3])
                    inp.set_name_para(usr_name)

            predicted_issue_ids = DecisiontreeController.decisontree_results(inp.get_component(), inp.get_category(),
                                                                             inp.get_input_array())
            rank = RankingController()
            issue_id = rank.process_decisiontree_result(predicted_issue_ids)
            print(issue_id)

            cat = inp.get_category()
            typ = inp.get_type()

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
            inp.set_component(component)

            if inp.get_component() == 'categorizing':
                if inp.get_category() == 'network':
                    q1 = input(net_cat_ques[0])
                    inp.set_question1(q1)

                    q2 = input(net_cat_ques[1])
                    inp.set_question2(q2)

                    q3 = input(net_cat_ques[2])
                    inp.set_question3(q3)

                    q4 = input(net_cat_ques[3])
                    inp.set_question4(q4)

                elif inp.get_category() == 'directory':
                    q1 = input(direct_cat_ques[0])
                    inp.set_question1(q1)

                    q2 = input(direct_cat_ques[1])
                    inp.set_question2(q2)

                    q3 = input(direct_cat_ques[2])
                    inp.set_question3(q3)

                    q4 = input(direct_cat_ques[3])
                    inp.set_question4(q4)

                elif inp.get_category() == 'user':
                    q1 = input(userconf_cat_ques[0])
                    inp.set_question1(q1)

                    q2 = input(userconf_cat_ques[1])
                    inp.set_question2(q2)

                    q3 = input(userconf_cat_ques[2])
                    inp.set_question3(q3)

                    q4 = input(userconf_cat_ques[3])
                    inp.set_question4(q4)

            predicted_solution_type = DecisiontreeController.decisontree_results(inp.get_component(),
                                                                                 inp.get_category(),
                                                                                 inp.get_input_array())
            solution_id = None
            # for key in predicted_issue_ids.keys():
            #  print(key)
            # issue_id = key
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

                elif solution_type == "tech":
                    solution_id = Queries.get_tech_solution_id_by_issue_id(issue_id)
                    permant_para = Queries.get_permenant_parameter_by_issue_id(issue_id)
                    if permant_para[0][0] != 'None':
                        print(permant_para[0][0])
                        inp.set_name_para(permant_para[0][0])
                    else:
                        print(solution_id[0][0])
                    # y = ScriptGenerator()
                    # y.process_sequence(solution_id[0][0])

                ranking_q = input(Questions.Ranking_question)  # ranking question after solution
                if 5 >= int(ranking_q) >= 1:
                    with open(rank_log_csv, newline='') as f1:
                        reader = csv.reader(f1)
                        row1 = next(reader)
                    f1.close()
                    print(row1)

                    w, x, y, z = row1[0], row1[1], row1[2], int(ranking_q)
                    csvRow = [w, x, y, z]
                    csvfile = issue_history_csv
                    with open(csvfile, "a", newline='') as fp:
                        wr = csv.writer(fp, dialect='excel')
                        wr.writerow(csvRow)
                    fp.close()

                    f3 = open(rank_log_csv, "w")
                    f3.truncate()
                    f3.close()

            # print(predicted_issue_ids)
            # split_by_issue = predicted_issue_ids.split(",")

            # for y in split_by_issue:
            #   split_by_issue_id = y.split(":")
            #   issue_id = split_by_issue_id[0]
            #  print(issue_id)
        else:
            ranking_q = input(Questions.Ranking_question)  # ranking question after reboot
            if 5 >= int(ranking_q) >= 1:
                with open(rank_log_csv, newline='') as f1:
                    reader = csv.reader(f1)
                    row1 = next(reader)
                f1.close()
                print(row1)

                w, x, y, z = row1[0], row1[1], row1[2], int(ranking_q)
                csvRow = [w, x, y, z]
                csvfile = issue_history_csv
                with open(csvfile, "a", newline='') as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(csvRow)
                fp.close()

                f3 = open(rank_log_csv, "w")
                f3.truncate()
                f3.close()
