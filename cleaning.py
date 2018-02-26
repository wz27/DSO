# g = open('data.txt', 'a+')
h = open('clean.txt', 'a+')

with open('data.txt') as g:
    data = g.readlines()

    for line in data:
        
        if "Timestamp" in line:
            pass
        else:
            h.write(line)

# g.close()
h.close()
