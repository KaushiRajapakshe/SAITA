from Controllers.Query import Queries
from Models.Inputs import Input


# Get database data for categorizing the issue to an array
def get_arr():
    inp = Input.get_input()
    if inp.get_component() == 'categorizing':
        if inp.get_category() == 'network':
            net_arr = []  # network data array
            result = Queries.get_all_networks_solution_category()  # categorizing result data from the database network table
            for x in result:
                pre_split_field = x[3]
                split_field = pre_split_field.split("/")
                for y in split_field:
                    a = [x[0], x[1], x[2], y, x[4]]
                    net_arr.append(a)

            print(net_arr)
            return net_arr
        elif inp.get_category() == 'directory':
            direct_arr = [] # directory data array
            result = Queries.get_all_directory_solution_category()  # categorizing result data from the database directory table
            for x in result:
                pre_split_field = x[3]
                split_field = pre_split_field.split("/")
                for y in split_field:
                    a = [x[0], x[1], x[2], y, x[4]]
                    direct_arr.append(a)

            print(direct_arr)
            return direct_arr
        elif inp.get_category() == 'user':
            user_arr = [] # user data array
            result = Queries.get_all_userconf_solution_category()  # categorizing result data from the database user table
            for x in result:
                pre_split_field = x[3]
                split_field = pre_split_field.split("/")
                for y in split_field:
                    a = [x[0], x[1], x[2], y, x[4]]
                    user_arr.append(a)

            print(user_arr)
            return user_arr
