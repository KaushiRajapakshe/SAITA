import csv
import random
from Models.Inputs import Input
from Data.Variables import *
from Util.Logistic_ranking import Logistic


class RankingController:
    inp = None
    max_rating = 0
    max_issueid = None

    def __init__(self):
        self.inp = Input.get_input()

    def process_decisiontree_result(self, result):
        all_values = result.values()
        max_value = max(all_values)  # get max value
        print([k for k, v in result.items() if v == max_value])
        maxissues = [k for k, v in result.items() if v == max_value]  # Issues with max percentage
        return self.choose_issue(maxissues)

    def choose_issue(self, issuelist):
        input_file = open(issue_history_csv, "r+")
        reader_file = csv.reader(input_file)
        rowNo = len(list(reader_file))  # get no of data in user issue history
        print(rowNo)

        last_data = []
        with open(issue_history_csv, 'r') as csvfile:
            so = csv.reader(csvfile, delimiter=',', quotechar='"')

            for row in so:
                last_data.append(row)

        last_data = last_data[-10:]  # get last 10 records from csv
        print(last_data)

        if rowNo < 60:  # check for enough history data
            usable_stat = 0
            countarr = []
            while usable_stat == 0:
                usable_stat = 1
                choiceid = random.choice(issuelist)
                print(choiceid)
                usable_stat = self.check_list_for_unusable(last_data, choiceid)
                #print(usable_stat)
                countarr.append(choiceid)
                # print(set(count).intersection(issuelist))
                # print(len(set(count).intersection(issuelist)))
                if len(set(countarr).intersection(issuelist)) == len(issuelist):# check whether the loop has run through all issues
                    usable_stat = 1

            # print(choiceid)
            return choiceid

        else:
            logist = Logistic()
            for issueid in issuelist:
                cat = self.inp.get_category()
                typ = self.inp.get_type()

                itype = None
                category = None
                if cat == 'network':
                    category = 1
                    if typ == 'intranet':
                        itype = 1
                    elif typ == 'internet':
                        itype = 2
                elif cat == 'directory':
                    category = 2
                    if typ == 'file':
                        itype = 3
                    elif typ == 'directory':
                        itype = 4
                    elif typ == 'drive':
                        itype = 5
                elif cat == 'user':
                    category = 3
                    if typ == 'local':
                        itype = 6

                rating = logist.ranking([category, itype, issueid])
                if rating[0] > self.max_rating:
                    self.max_issueid = issueid
                    self.max_rating = rating

            print(self.max_issueid)
            # print(self.max_rating)
            return self.max_issueid

    def check_list_for_unusable(self, alist, issueid):  # check last records for poor ratings for a issueid

        for item in alist:
            #print(item)
            #print(int(item[2]) == int(issueid) and int(item[3]) == 1)
            if int(item[2]) == int(issueid) and int(item[3]) == 1:
                return 0

        return 1
