j = open('stage04Single.txt', 'w')
k = open('stage04Others.txt', 'w')
g = open('stage04.txt', 'w')
filename = 'stage03.txt'
f = open(filename)
data = f.readlines()
index = 0
subjList = set()
for index in range(0, len(data)):
    dummy = data[index].split(",")
    subjList.add(dummy[5].upper().replace("FW: ", "").replace("RE: ", ""))

#new text file, array of email line numbers, followed by subj that is similar
for subj in subjList:
    count = []
    with open(filename) as h:
        data2 = h.readlines()
        for index2 in range(0, len(data2)):
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

    g.write(subjdrop + "\n" + "Size of block: " + length + " First: " + firstDate + " " + firstTime + ", Last: " + lastDate + " " + lastTime + "\n")
    for i in count:
        g.write(data[i] + "\n")
    # subj has \n at the back.
    if length == '1':
        j.write(subjdrop + "\n" + "Size of block: " + length + " First: " + firstDate + " " + firstTime + ", Last: " + lastDate + " " + lastTime + "\n")
        for i in count:
            j.write(data[i] + "\n")
    else:
        k.write(subjdrop + "\n" + "Size of block: " + length + " First: " + firstDate + " " + firstTime + ", Last: " + lastDate + " " + lastTime + "\n")
        for i in count:
            k.write(data[i] + "\n")


f.close()
g.close()
j.close()
