from Controllers import CategorizerData, IdentifyingData
from Models.Inputs import Input


"""results = []

with open("network.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)  # change contents to floats
    for row in reader:  # each row is a list
        results.append(row)"""


def check_com():
    inp = Input.get_input()
    if inp.get_component() == 'categorizing':
        # network_category_data = results
        return CategorizerData.get_arr()
    elif inp.get_component() == 'identifying':
        return IdentifyingData.get_arr()


# print(results)
# network_identify_data = []

