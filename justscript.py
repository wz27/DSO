f = open('tmp335.txt', 'w')

g = open('stage04Others.txt')
data = g.readlines()
for index in range(0, len(data)):
  if "@dso.org.sg" in data[index]:
    f.write(data[index])
  else:
    pass

f.close()
g.close()
