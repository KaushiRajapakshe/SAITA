import DBConnection
import Inputs

if Inputs.component == 'identifying':
    net_arr = []

    # query = "SELECT a,b,c,d,result FROM net"

    result = DBConnection.z

    for x in result:

        pre_split_field = x[2]
        split_field = pre_split_field.split("/")
        # print(len(split_field))
        for y in split_field:
            a = [x[0], x[1], y, x[3]]

            net_arr.append(a)

    print(net_arr)
