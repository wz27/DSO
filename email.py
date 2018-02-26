g = open('senderDSO.txt', 'w')
f = open('senderNon.txt', 'w')
k = open('receiverDSO.txt', 'w')
j = open('receiverNon.txt', 'w')

h = open('stage03.txt', 'r')
data = h.readlines()
index = 0
for index in range(0, len(data)):
    dummy = data[index].split(",")

    x = dummy[2].lower().find("dso")
    y = dummy[4].lower().find("dso")

    if x != -1:
        k.write(dummy[2] + "\n")
    else:
        j.write(dummy[2] + "\n")

    if y != -1:
        g.write(dummy[4] + "\n")
    else:
        f.write(dummy[4] + "\n")

g.close()
f.close()
k.close()
j.close()
h.close()
