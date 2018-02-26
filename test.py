import datetime

g = open("stage01.txt", "w")
# with open('formatted.txt') as g:
filename = 'clean.txt'

with open(filename) as f:
    data = f.readlines()
    # index = 0
    # subjList = set()
    for index in range (0, 691531):
    # for index in range (0, 200):

        dummy = data[index].split(",")
        # subjList.add(dummy[4])

        # print(dummy[0])

        dateTime = dummy[0].split(" ")
        date = dateTime[1].strip("\"")
        # print(date.strip("\""))
        dmy = date.split("/")
        day = dmy[0]
        month = dmy[1]
        # print(index)
        year = dmy[2]
        if len(day) == 1:
            day = "0" + day
        else:
            pass
        date2 = day + "/" + month + "/" + year
        fDate = datetime.datetime.strptime(date2, '%d/%m/%Y').strftime('%Y/%m/%d')
        # print(fDate)

        hour = dateTime[2].split(":")[0]
        minute = dateTime[2].split(":")[1]
        second = dateTime[2].split(":")[2]
        inthour = int(hour)
        ampm = dateTime[3].strip("\"")
        if ampm == "PM":
            inthour += 12
        else:
            pass
        # print(str(inthour))

        # subj = dummy[4].upper()
        # dropapostF = subj.lstrip("\"")
        # dropapost = subj.strip("\"")
        # dropRE = dropapost.strip("RE:")
        # dropRE2 = dropRE.strip("RE:")
        # dropFW = dropRE2.strip("FW:")
        # droplast = dropFW.strip("\"")

        droplast = dummy[4].strip("\n").strip("\"")
        # print(index)


        output = fDate + "," + str(inthour) + ":" + minute + ":" + second + "," + dummy[1] + "," + dummy[2] + "," + dummy[3] + "," + droplast + "\n"

        g.write(output)
        # count = str(index)
        # count = open("formatted.txt", "r")
        # lines = count.readlines()
        # count.close()
        # outputTest = output
        # if outputTest in lines:
        #     pass
        # else:
        #     count = open("formatted.txt", "a")
        #     count.write(outputTest)




# with open('formatted.txt', 'a+') as g:
#
#     if output in g:
#         pass
#             # print(already)
#     else:
#         g.write(output)

# print(already[3])

        # count.close()
g.close()
