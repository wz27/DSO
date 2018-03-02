g = open('nonspam.txt')
data = g.readlines()

h = open('stage06.txt', 'w')

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

    users = set()
    index3 = 0
    for line in range(0, len(count)):
        if ";" in data[count[line]].split(",")[2]:
            separate = data[count[line]].split(",")[2].split(";")
            for index4 in range(0, len(separate)):
                users.add(separate[index4].replace("\"", "").replace("\'", ""))
        else:
            users.add(data[count[line]].split(",")[2].replace("\"", "").replace("\'", ""))

        if ";" in data[count[line]].split(",")[4]:
            separate = data[count[line]].split(",")[4].split(";")
            for index4 in range(0, len(separate)):
                users.add(separate[index4].replace("\"", "").replace("\'", ""))
        else:
            users.add(data[count[line]].split(",")[4].replace("\"", "").replace("\'", ""))

    legend = 0
    mydict = {}
    for user in users:
        mydict[user] = legend
        legend += 1

    h.write(subj + str(mydict) + "\n")

    for line in range(0, len(count)):
        if ";" in data[count[line]].split(",")[4]:
            separate = data[count[line]].split(",")[4].split(";")
            for index4 in range(0, len(separate)):
                h.write(str(mydict[(separate[index4].replace("\"", "").replace("\'", ""))]) + "->")
        else:
            h.write(str(mydict[(data[count[line]].split(",")[4].replace("\"", "").replace("\'", ""))]) + "->")

        if ";" in data[count[line]].split(",")[2]:
            separate = data[count[line]].split(",")[2].split(";")
            for index4 in range(0, len(separate)):
                h.write(str(mydict[(separate[index4].replace("\"", "").replace("\'", ""))]))
        else:

            h.write(str(mydict[(data[count[line]].split(",")[2].replace("\"", "").replace("\'", ""))]))
        h.write(" "+ data[count[line]].split(",")[0] + " " + data[count[line]].split(",")[1] + " " + data[count[line]].split(",")[3] + "\n")
