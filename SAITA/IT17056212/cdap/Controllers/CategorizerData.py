from Controllers.Query import Queries
from Models.Inputs import Input


def get_arr():
    inp = Input.get_input()
    if inp.get_component() == 'categorizing':
        if inp.get_category() == 'network':
            #print("cat cat" + inp.get_component())
            #print("cat cat" + inp.get_category())
            net_arr = []

            result = Queries.get_all_networks_solution_category()

            for x in result:

                pre_split_field = x[3]
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], x[1], x[2], y, x[4]]
                    net_arr.append(a)

            print(net_arr)
            return net_arr
        elif inp.get_category() == 'directory':
            # print("cat cat" + inp.get_component())
            # print("cat cat" + inp.get_category())
            direct_arr = []

            result = Queries.get_all_directory_solution_category()

            for x in result:

                pre_split_field = x[3]
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], x[1], x[2], y, x[4]]
                    direct_arr.append(a)

            print(direct_arr)
            return direct_arr
        elif inp.get_category() == 'user':
            # print("cat cat" + inp.get_component())
            # print("cat cat" + inp.get_category())
            user_arr = []

            result = Queries.get_all_userconf_solution_category()

            for x in result:

                pre_split_field = x[3]
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], x[1], x[2], y, x[4]]
                    user_arr.append(a)

            print(user_arr)
            return user_arr
