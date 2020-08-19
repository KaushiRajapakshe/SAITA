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
        return CategorizerData.get_netarr()
    elif inp.get_component() == 'identifying':
        return IdentifyingData.get_netarr()


# print(results)
# network_identify_data = []

directory_category_data = [
    ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'non-tech'],
    ['yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'tech'],
    ['no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'tech'],
    ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'non-tech'],
    ['no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'tech'],
    ['no', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'tech'],
    ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'non-tech'],
    ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'non-tech'],
    ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'tech'],
    ['no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'tech'],
    ['no', 'yes', 'no', 'no', 'yes', 'no', 'no', 'no', 'non-tech'],
    ['no', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'tech'],
    ['no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'tech'],
    ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'non-tech'],
    ['no', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'tech'],
    ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'non-tech'],
    ['bo', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'non-tech'],
    ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'tech'],
    ['yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'tech'],
    ['no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'non-tech'],
    ['no', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'tech'],
    ['no', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'tech'],
    ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'non-tech']
]
