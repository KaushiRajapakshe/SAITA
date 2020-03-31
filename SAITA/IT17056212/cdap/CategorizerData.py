import DBConnection
import Inputs

if Inputs.component == 'categorizing':
    net_arr = []

    # query = "SELECT a,b,c,d,result FROM net"

    result = DBConnection.y

    for x in result:

        pre_split_field = x[3]
        split_field = pre_split_field.split("/")
        # print(len(split_field))
        for y in split_field:
            a = [x[0], x[1], x[2], y, x[4]]
            net_arr.append(a)

    print(net_arr)
