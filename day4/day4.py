file = "day4/day4.txt"

total = []

# finds the point value for each card for the given number (n) of matches we have
def value(n):
    # the very convenient formula is 1 x 2^(n-1)
    points = 1 * 2 ** (n-1)
    total.append(points)

with open (file, 'r') as f:
    
    for line in f:
        
        # neatly organizes the input into two sets per line, the left of the pipe and right of the pipe
        offset = line.rfind(":") + 2
        shrunk = line[offset:-1]
        mlist = shrunk.split(" ")
        while mlist.count(""):
            mlist.remove("")

        alist = set(mlist[:(mlist.index("|"))])

        zlist = set(mlist[(mlist .index("|") + 1):])
        
        # finds the matches
        n = len(alist.intersection(zlist))
        
        if n != 0:
            value(n)
        
    print(total)
    print(sum(total))