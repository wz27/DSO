h = open("stage02.txt", "r+")
g = open("stage03.txt", "w")
lines = h.readlines()
total = len(lines)
prev_line = lines[0]
g.write(prev_line)
for index in range(1, total):
#for index in range(1, 4000):
    if lines[index] != prev_line:
        prev_line = lines[index]
        g.write(lines[index])
g.close()
h.close()
