from Controllers import CategorizerData, IdentifyingData
from Models.Inputs import Input


# Get the results of categorizing & identifying controllers
def check_com():
    inp = Input.get_input()
    if inp.get_component() == 'categorizing':
        return CategorizerData.get_arr()
    elif inp.get_component() == 'identifying':
        return IdentifyingData.get_arr()
