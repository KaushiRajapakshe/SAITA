from Controllers.Query import Queries
from Models.Inputs import Input
from difflib import SequenceMatcher


# Get database data for identifying the issue to an array
def get_arr():
    inp = Input.get_input()
    if inp.get_component() == 'identifying':
        if inp.get_category() == 'network':
            # print("ident cat" + inp.get_component())
            # print("ident cat" + inp.get_category())
            net_arr = []

            result = Queries.get_all_networkerrors()  # identifying result data from the database network table
            # print(result)
            for x in result:

                # compare similarity ratio
                errormsg = x[0]
                ratio = SequenceMatcher(None, errormsg, inp.get_error_msg()).ratio()
                if ratio > 0.5:
                    x = list(x)
                    x[0] = inp.get_error_msg()
                    x = tuple(x)
                    print('Changed after similarity check: ' + x[0])
                else:
                    x = list(x)
                    x[0] = errormsg
                    x = tuple(x)

                pre_split_field = x[1].lower() + "/" + "none"
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], y, x[2], x[3]]

                    net_arr.append(a)

            print(net_arr)
            return net_arr
        elif inp.get_category() == 'directory':
            direct_arr = []

            result = Queries.get_all_directoryerrors()  # identifying result data from the database directory table
            # print(result)
            for x in result:

                # compare similarity ratio
                errormsg = x[0]
                ratio = SequenceMatcher(None, errormsg, inp.get_error_msg()).ratio()
                if ratio > 0.5:
                    x = list(x)
                    x[0] = inp.get_error_msg()
                    x = tuple(x)
                    print('Changed after similarity check: ' + x[0])
                else:
                    x = list(x)
                    x[0] = errormsg
                    x = tuple(x)

                pre_split_field = x[1].lower() + "/" + "none"
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], y, x[2], x[3]]

                    direct_arr.append(a)

            print(direct_arr)
            return direct_arr

        elif inp.get_category() == 'user':
            userconf_arr = []

            result = Queries.get_all_userconferrors()  # identifying result data from the database user table
            # print(result)
            for x in result:

                # compare similarity ratio
                errormsg = x[0]
                ratio = SequenceMatcher(None, errormsg, inp.get_error_msg()).ratio()
                if ratio > 0.5:
                    x = list(x)
                    x[0] = inp.get_error_msg()
                    x = tuple(x)
                    print('Changed after similarity check: ' + x[0])
                else:
                    x = list(x)
                    x[0] = errormsg
                    x = tuple(x)

                pre_split_field = x[1].lower() + "/" + "none"
                split_field = pre_split_field.split("/")
                # print(len(split_field))
                for y in split_field:
                    a = [x[0], y, x[2], x[3]]

                    userconf_arr.append(a)

            print(userconf_arr)
            return userconf_arr
