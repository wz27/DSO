# want to modify script from 23-2 but cannot run 23-2 again as it takes too long
'''
pseudocode

open tmp334

process again and group together using subject

for subject_list if only one unique sender appears for all lines of email:
    write subject_list into spam.txt

    else:
        write into notspam.txt

'''
a = open('spam.txt', 'w')
b = open('nonspam.txt', 'w')


g = open('tmp335.txt')
data = g.readlines()
subjList = set()

for index in range(0, len(data)):
    dummy = data[index].split(",")
    subjList.add(dummy[5].upper().replace("FW: ", "").replace("RE: ", ""))

for subj in subjList:
    count = []
    for index2 in range(0, len(data)):
        dummy2 = data[index2].split(",")
        if dummy2[5].upper().replace("FW: ", "").replace("RE: ", "") == subj:
            count.append(index2)
        else:
            pass

    sender = data[count[0]].split(",")[4]
    # print(count)
    for line in range(0, len(count)):
        if data[count[line]].split(",")[4] == sender:
            a.write(data[count[line]])
        else:
            b.write(data[count[line]])

a.close()
b.close()
g.close()
