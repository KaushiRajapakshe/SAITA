import csv
import CategorizerData
import IdentifyingData
import Inputs

results = []
with open("network.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)  # change contents to floats
    for row in reader:  # each row is a list
        results.append(row)

if Inputs.component == 'categorizing':
    #network_category_data = results
    network_category_data = CategorizerData.net_arr
elif Inputs.component == 'identifying':
    network_identify_data = IdentifyingData.net_arr





# print(results)
#network_identify_data = []

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
