from Inputs import Input
from Decisiontree_controller import DecisiontreeController
from Query import Queries
from Sentence_Controller import SentenceController

inp = Input.get_input()

if __name__ == '__main__':

    category = input("Category: ")
    inp.set_category(category)

    component = 'identifying'
    inp.set_component(component)

    if inp.get_component() == 'identifying':
        if inp.get_category() == 'network':
            msg = input("msg: ")
            inp.set_error_msg(msg)

            code = input("code: ")
            inp.set_error_code(code)

            type = input("type: ")
            inp.set_type(type)

    predicted_issue_ids = DecisiontreeController.decisontree_results(inp.get_component(), inp.get_category(),
                                                                     inp.get_input_array())
    component = 'categorizing'
    inp.set_component(component)

    if inp.get_component() == 'categorizing':
        if inp.get_category() == 'network':
            q1 = input("Q1: ")
            inp.set_question1(q1)

            q2 = input("Q2: ")
            inp.set_question2(q2)

            q3 = input("Q3: ")
            inp.set_question3(q3)

            q4 = input("Q4: ")
            inp.set_question4(q4)

    predicted_solution_type = DecisiontreeController.decisontree_results(inp.get_component(), inp.get_category(),
                                                                         inp.get_input_array())
    solution_id = None
    for key in predicted_issue_ids.keys():
        print(key)
        issue_id = key
        for key2 in predicted_solution_type.keys():
            print(key2)
            solution_type = key2
            if solution_type == "non-tech":
                solution_id = Queries.get_network_nontech_solution_id_by_issue_id(issue_id)

                print(solution_id[0][0])
                nontech_keyward = Queries.get_keywards_by_nontech_solution_id(solution_id[0][0])
                sentence = SentenceController.sentence_generator_results(nontech_keyward)
                print("Main Output: " + sentence)

            elif solution_type == "tech":
                solution_id = Queries.get_network_tech_solution_id_by_issue_id(issue_id)



    # print(predicted_issue_ids)
    # split_by_issue = predicted_issue_ids.split(",")

    # for y in split_by_issue:
    #   split_by_issue_id = y.split(":")
    #   issue_id = split_by_issue_id[0]
    #  print(issue_id)
