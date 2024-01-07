file = "day4/day4.txt"

total = []
cards = []
instances = []

# finds the matches for a given line
def findmatches(line):
    # neatly organizes the input into two sets per line, the left of the pipe and right of the pipe
    offset = line.rfind(":") + 2
    shrunk = line[offset:-1]
    mlist = shrunk.split(" ")
    while mlist.count(""):
        mlist.remove("")

    alist = set(mlist[:(mlist.index("|"))])

    zlist = set(mlist[(mlist .index("|") + 1):])
    
    # actually finds the matches
    n = len(alist.intersection(zlist))
    
    return n

# creates the list of lists from the input
with open (file, 'r') as f:
    
    for line in f:
        
        offset = line.rfind(":")
        shrunk = line[:offset]
        cards.append(shrunk)
        instances.append(1)
        
    zipped = [list(x) for x in zip(cards, instances)]
        
# uses the list of lists to find the amount of copies of each card we should have
with open (file, 'r') as f:
    
    for count, line in enumerate(f):
        # finds the cards that copies will be added to
        nextcards = zipped[count + 1 : findmatches(line) + count + 1]
        # gets the copies of the card we are currently on
        copies = zipped[count][1]
        # adds the copies to the relevant cards
        for x in nextcards:
            x[1] = x[1] + copies
        total.append(copies)
        
print(zipped)
print(total)
print(sum(total))