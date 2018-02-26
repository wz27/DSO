g = open('cat.txt')
filename = 'sorted.txt'
f = open(filename)
data = f.readlines()
index = 0
subjList = set()
for index in range(0, 691530):
    dummy = data[index].split(",")
    subjList.add(dummy[5].upper().replace("FW: ", "").replace("RE: ", ""))

#new text file, array of email line numbers, followed by subj that is similar
for subj in subjList:
    count = []
    with open(filename) as g:
        data2 = g.readlines()
        for index2 in range(0, 691530):
            dummy2 = data2[index2].split(",")
            if dummy2[5].upper().replace("FW: ", "").replace("RE: ", "") == subj:
                count.append(index2)
            else:
                pass
    array = str(count).strip("\n")
    length = str(len(count))
    subjdrop = subj.strip("\n")

    firstLine = count[0]
    firstDate = str(data[firstLine].split(",")[0])
    firstTime = str(data[firstLine].split(",")[1])

    lastLine = count[-1]
    lastDate = str(data[lastLine].split(",")[0])
    lastTime = str(data[lastLine].split(",")[1])

    g.write("#lines=" + length + ": " + array + ": " + subjdrop + ", " + "First: " + firstDate + " " + firstTime + ", Last: " + lastDate + " " + lastTime)
    # subj has \n at the back.

f.close()
g.close()
