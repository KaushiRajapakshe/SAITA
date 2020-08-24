from Util import Decision_tree
from Controllers import Datasets
from Data import Questions


class DecisiontreeController:

    @classmethod
    def decisontree_results(cls, component, category, input_array):
        if component == 'categorizing':
            if category == 'network':
                training_data = Datasets.check_com()
                Decision_tree.header = Questions.network_categorizing_questions
            elif category == 'directory':
                training_data = Datasets.check_com()
                Decision_tree.header = Questions.directory_categorizing_questions
            elif category == 'user':
                training_data = Datasets.check_com()
                Decision_tree.header = Questions.userconf_categorizing_questions
            else:
                Decision_tree.header = []
        elif component == 'identifying':
            if category == 'network':
                training_data = Datasets.check_com()
                Decision_tree.header = Questions.network_identifying_questions
            elif category == 'directory':
                training_data = Datasets.check_com()
                Decision_tree.header = Questions.directory_identifying_questions
            elif category == 'user':
                training_data = Datasets.check_com()
                Decision_tree.header = Questions.userconf_identifying_questions
            else:
                Decision_tree.header = []
        else:
            Decision_tree.header = []

        testing_data = input_array

        my_tree = Decision_tree.build_tree(training_data)

        Decision_tree.print_tree(my_tree)
        # print(questions_array)
        # Evaluate
        testing_data = input_array

        for row in testing_data:
            print("Actual: %s. Predicted: %s" %
                  (row[-1], Decision_tree.print_leaf(Decision_tree.classify(row, my_tree))))

            return Decision_tree.print_leaf(Decision_tree.classify(row, my_tree))
