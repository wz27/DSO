"""
import igraph

g = open('stage06.txt')
class eline:

    def __init__(self, date, time, receiver, sender, type, subject):
        self.date = date
        self.time = time
        self.receiver = receiver
        self.sender = sender
        self.type = type
        self.subject = subject

line1 = eline(various params)
line2 = eline(various params)

for lines in each block:
    def relation(line1.receiver, line1.sender, line2.receiver, line2.sender):
        if line1.receiver == line2.sender and line2.date >= line1.date (find way to represent both date and time):
            graph = Graph()
            graph.add_vertices(2)
            graph.add_edges([(0,1)])
            return graph

    call relation combinatorically thru block
    repeat on relations until no new relations can be made

another option:
    insert -> between numbers
    select first one from list then compare with all below
    if length more than 1:
        return
    then move on to next eline and compare with all below

    dont need to plot graph first, just output 0->1->2-> etc.

assumed format:
0->1
1->2/3/4
"""
g = open('testR.txt')
data = g.readlines()

"""
# for option in options:
def looper(index):
    options = ['']
    for index in range(index, len(data)):
        sender = data[index].split("->")[0]
        if options == ['']:
            prev = '->' + sender
            options = data[index].split("->")[1].replace('\n', '').split('/')
            for option in options:
                looper(index+1)
        elif sender in options:
            prev = prev + '->' + sender
            print(prev)
            options = data[index].split("->")[1].replace('\n', '').split('/')
            for option in options:
                looper(index+1)
looper(0)
"""
# for index in range(0, len(data)):
#     sender = data[index].split("->")[0]
#     receiver = data[index].split("->")[1].strip('\n').split('/')
#     for index2 in range(index+1, len(data)):
#         chain = [sender] # one chain for each comparison
#         sender2 = data[index2].split("->")[0]
#         receiver2 = data[index2].split("->")[1].strip('\n').split('/')
#         if sender2 in receiver:
#             chain.append(sender2)
#         for index3 in range(index2+1, len(data)):
#              # one chain for each comparison
#             sender3 = data[index3].split("->")[0]
#             receiver3 = data[index3].split("->")[1].strip('\n').split('/')
#             if sender3 in receiver2:
#                 chain.append(sender3)
#             for index4 in range(index3+1, len(data)):
#                  # one chain for each comparison
#                 sender4 = data[index4].split("->")[0]
#                 receiver4 = data[index4].split("->")[1].strip('\n').split('/')
#                 if sender4 in receiver3:
#                     chain.append(sender4)
#             print(chain)
#
#
# g.close()
# #
# index = 0
# for index in range(0, len(data)):
#     sender0 = data[index].split("->")[0]
#     chain = [sender0]
#     receiver = data[index].split("->")[1].strip('\n').split('/')
#     for index2 in range(index+1, len(data)):
#         for alt in receiver:
#             sender = data[index2].split("->")[0]
#             if sender == alt:
#                 chain.append(sender)
#                 receiver = data[index2].split("->")[1].strip('\n').split('/')
#     print(chain)
# g.close()



# index = 0
# def recursion(index):
#     while index < len(data):
#         sender0 = data[index].split("->")[0]
#         chain = [sender0]
#         receiver = data[index].split("->")[1].strip('\n').split('/')
#         for index2 in range(index+1, len(data)):
#             for alt in receiver:
#                 sender = data[index2].split("->")[0]
#                 if sender == alt:
#                     chain.append(sender)
#                     # receiver = data[index2].split("->")[1].strip('\n').split('/')
#                 recursion(index2)
#         print(chain)
#         index += 1
# recursion(index)
# g.close()


def recur(receiver):
    for index2 in range(index+1, len(data)):
        for alt in receiver:
            sender = data[index2].split("->")[0]
            if sender == alt:
                chain.append(sender)
                receiver = data[index2].split("->")[1].strip('\n').split('/')
                collection.append(chain)

for index in range(0, len(data)):
    sender0 = data[index].split("->")[0]
    collection = []
    chain = [sender0]
    receiver = data[index].split("->")[1].strip('\n').split('/')
    recur(receiver)

    print(collection)
g.close()
