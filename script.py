# Script for finding relationships between emails
# importing modules

from difflib import SequenceMatcher
import datetime

# import emails as vector
import pandas as pd
emails = pd.read_csv('1453345192630-1')
print(emails.shape) # output email vector shape

# import emails iteratively
filename = 'data.txt'
with open(filename) as f:
    data = f.readlines()
    index = 0
    subjList = set()
    for index in range (0, 9):
        dummy = data[index].split(",")
        subjList.add(dummy[4])

        # print(dummy[0])

        dateTime = dummy[0].split(" ")
        date = dateTime[1].strip("\"")
        # print(date.strip("\""))
        fDate = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%y/%m/%d')
        print(fDate)

        hour = dateTime[2].split(":")[0]
        inthour = int(hour)
        ampm = dateTime[3].strip("\"")
        if ampm == "PM":
            inthour += 12
        else:
            pass
        print(str(inthour))


# get time formatted, add 12 hours for PM (store time in variable first)
# write new file in data.txt with formatted date and time
# then sort
# new python script to sort data into new txt file, so all lines are sorted by time already.


    # print(subjList[8])
    # refined0 = data[0].split(",")
    # refined1 = data[1].split(",")
    # print(refined0[1]) #check

# find string similarity between email subject Lines
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

import operator

my_dict = {}
for subj in subjList:

    my_dict[subj] = [] #change to [] if can assume logs are in time order already
    with open(filename) as g:
        data2 = g.readlines()
        index2 = 0
        for index2 in range (0, 9):
            dummy2 = data2[index2].split(",")
            if similar(dummy2[4], subj) >= 0.9:
                # my_dict.get(subj)[index2] = dummy2[0]
                # print(my_dict)

                # sortTime = sorted(my_dict.get(subj).items(), key=operator.itemgetter(1))
                # print(sortTime)

                #use this if can assume logs are in time order already.
                my_dict.get(subj).append(index2)

print(my_dict)


# firstSubj = refined0[4]
# secSubj = refined1[4]
# print(similar(firstSubj, secSubj))

# similarStrings = []
# def compare():
#     global similarStrings
#     counter1 = 0
#     counter2 = 0
#     for counter1 in range(0, 9):
#         for counter2 in range(0, 9):
#             similarity = similar(subjList[counter1], subjList[counter2])
#             if similarity >= 0.9 and counter1 != counter2:
#                 similarStrings.append([counter1, counter2])
#             else:
#                 pass
#     # clean up duplicate pairs and combine pairs
#     for pair in similarStrings:
#         value1 = pair[0]
#         value2 = pair[1]
#         if [value2, value1] in similarStrings:
#             similarStrings.remove([value2, value1])
#         else:
#             pass
#
#     return similarStrings
# compare()
# print(similarStrings)

# new function
# def dupedSubj():
#     global subjList
#     counter1 = 0
#     counter2 = 1
#     while counter1 <= 8:
#         while counter2 <= 8:
#             similarity = similar(subjList[counter1], subjList[counter2])
#             if similarity >= 0.9:
#                 subjList.remove(subjList[counter2])
#             else:
#                 pass
#             counter2 += 1
#         counter1 += 1
#     return subjList
#
# dupedSubj()


# print(subjList)
# print(len(subjList))







#compare timestamp
def time():
    for pair in similarStrings:
        value1 = pair[0]
        value2 = pair[1]
