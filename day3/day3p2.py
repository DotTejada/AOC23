import re

masterlist = []
gearlist = []
anslist = []
array = []
symbols = []

pattern = r'(\*)'

filename = "day3\\day3.txt"

# makes a 2D array with the input 
with open(filename, 'r') as f:
    for line in f.readlines():
        array.append(line.strip().split(' '))

# creates the multi-digit numbers for adding into the answer
def combine_numbers(numbers):
    combined_number = int(''.join(map(str, numbers)))
    
    return combined_number

# finds all the relevant symbols in the given line
def findsymbols(symbolindex, line):
    for count, ele in enumerate(array[line][0]):
        symbol = re.findall(pattern, ele)
        if symbol:
            symbol = str(symbol[0])
            symbols.append(symbol)
            symbolindex.append(count)
            
    return symbolindex

# finds all the numbers to the left and right of each symbol
def leftright(line, index):
    
    lnum = []
    rnum = []
         
    increm = 1
    while increm < 4:
        if index - increm >= 0:
            if array[line][0][index - increm].isdigit():
                print("left number at", str(index - increm))
                lnum.append(int(array[line][0][index - increm]))
                increm += 1
            else:
                break
        else:
            break
    lnum = list(reversed(lnum))
    if lnum:
        lnum = combine_numbers(lnum)
        gearlist.append(lnum)
        print(lnum)
        
    increm = 1
    while increm < 4:
        if index + increm <= defrange:
            if array[line][0][index + increm].isdigit():
                print("right number at", str(index + increm))
                rnum.append(int(array[line][0][index + increm]))
                increm += 1
            else:
                break
        else:
            break
    if rnum:
        rnum = combine_numbers(rnum)
        gearlist.append(rnum)
        print(rnum)
    increm = 1

# finds all the numbers above and diagonally above each symbol
def up(line, index):
    
    upleftnum = []
    uprightnum = []
        
    #initial check up
    increm = 1
    if array[line - 1][0][index].isdigit():
        print("up number at", str(index))
        temp = int(array[line - 1][0][index])
        #checks left
        increm = 1
        while increm < 4:
            if index - increm >= 0:
                if array[line - 1][0][index - increm].isdigit():
                    print("left number at", str(index - increm))
                    upleftnum.insert(0, int(array[line - 1][0][index - increm]))
                    increm += 1
                else:
                    break
            else:
                break

        #checks right
        increm = 1
        while increm < 4:
            if index + increm <= defrange:
                if array[line - 1][0][index + increm].isdigit():
                    print("right number at", str(index + increm))
                    uprightnum.append(int(array[line - 1][0][index + increm]))
                    increm += 1
                else:
                    break
            else:
                break
            
        if upleftnum and uprightnum:
            upleftnum.append(uprightnum[0])
            upleftnum.insert(1, temp)
            upleftnum = combine_numbers(upleftnum)
            gearlist.append(upleftnum)
            print(upleftnum)
            
        elif upleftnum:
            upleftnum.append(temp)
            upleftnum = combine_numbers(upleftnum)
            gearlist.append(upleftnum)
            print(upleftnum)
            
        elif uprightnum:
            uprightnum.insert(0, temp)
            uprightnum = combine_numbers(uprightnum)
            gearlist.append(uprightnum)
            print(uprightnum)
            
        elif temp:
            gearlist.append(temp)
            print(temp)
            
    else:
        #checks left
        increm = 1
        while increm < 4:
            if index - increm >= 0:
                if array[line - 1][0][index - increm].isdigit():
                    print("upleft number at", str(index - increm))
                    upleftnum.insert(0, int(array[line - 1][0][index - increm]))
                    increm += 1
                else:
                    break
            else:
                break
            
        if upleftnum:
            upleftnum = combine_numbers(upleftnum)
            gearlist.append(upleftnum)
            print(upleftnum)
            

        #checks right
        increm = 1
        while increm < 4:
            if index + increm <= defrange:
                if array[line - 1][0][index + increm].isdigit():
                    print("upright number at", str(index + increm))
                    uprightnum.append(int(array[line - 1][0][index + increm]))
                    increm += 1
                else:
                    break
            else:
                break
                
        if uprightnum:
            uprightnum = combine_numbers(uprightnum)
            gearlist.append(uprightnum)
            print(uprightnum)

# finds all the numbers below and diagonally below each symbol
def down(line, index):
    
    downleftnum = []
    downrightnum = []
        
    #initial check down
    increm = 1
    if array[line + 1][0][index].isdigit():
        print("down number at", str(index))
        temp = int(array[line + 1][0][index])
        
        #checks left
        while increm < 4:
            if index - increm >= 0:
                if array[line + 1][0][index - increm].isdigit():
                    print("left number at", str(index - increm))
                    downleftnum.insert(0, int(array[line + 1][0][index - increm]))
                    increm += 1
                else:
                    break
            else:
                break
            
        #checks right
        increm = 1
        while increm < 4:
            if index + increm <= defrange:
                if array[line + 1][0][index + increm].isdigit():
                    print("right number at", str(index + increm))
                    downrightnum.append(int(array[line + 1][0][index + increm]))
                    increm += 1
                else:
                    break
            else:
                break
            
        if downleftnum and downrightnum:
            downleftnum.append(downrightnum[0])
            downleftnum.insert(1, temp)
            downleftnum = combine_numbers(downleftnum)
            gearlist.append(downleftnum)
            print(downleftnum)
            
            
        elif downleftnum:
            downleftnum.append(temp)
            downleftnum = combine_numbers(downleftnum)
            gearlist.append(downleftnum)
            print(downleftnum)
            
            
        elif downrightnum:
            downrightnum.insert(0, temp)
            downrightnum = combine_numbers(downrightnum)
            gearlist.append(downrightnum)
            print(downrightnum)
            
        
        elif temp:
            gearlist.append(temp)
            print(temp)
            
            
    else:
        #checks left
        increm = 1
        while increm < 4:
            if index - increm >= 0:
                if array[line + 1][0][index - increm].isdigit():
                    print("downleft number at", str(index - increm))
                    downleftnum.insert(0, int(array[line + 1][0][index - increm]))
                    increm += 1
                else:
                    break
            else:
                break
            
        if downleftnum:
            downleftnum = combine_numbers(downleftnum)
            gearlist.append(downleftnum)
            print(downleftnum)
            
        
        #checks right
        increm = 1
        while increm < 4:
            if index + increm <= defrange:
                if array[line + 1][0][index + increm].isdigit():
                    print("downright number at", str(index + increm))
                    downrightnum.append(int(array[line + 1][0][index + increm]))
                    increm += 1
                else:
                    break
            else:
                break
            
        if downrightnum:
            downrightnum = combine_numbers(downrightnum)
            gearlist.append(downrightnum)
            print(downrightnum)

# figures out which functions to use for each line, as well as making sure only gear ratios get added to the answer
with open(filename, 'r') as f:
    line = 0
    range = 140
    while line < range:
        
        symbolindex = []
        defrange = len(array[line][0]) - 1
        
        if line - 1 < 0:
            symbolindex = findsymbols(symbolindex, line) 
            for index in symbolindex:
                gearlist = []
                leftright(line, index)
                down(line, index)
                if len(gearlist) == 2:
                    ratio = gearlist[0] * gearlist[1]
                    masterlist.append(ratio)
            line += 1
        if line + 1 < range:
            symbolindex = findsymbols(symbolindex, line) 
            for index in symbolindex:
                gearlist = []
                leftright(line, index)
                up(line, index)
                down(line, index)
                if len(gearlist) == 2:
                    ratio = gearlist[0] * gearlist[1]
                    masterlist.append(ratio)
            line += 1
        else:
            symbolindex = findsymbols(symbolindex, line) 
            for index in symbolindex:
                gearlist = []
                leftright(line, index)
                up(line, index)
                if len(gearlist) == 2:
                    ratio = gearlist[0] * gearlist[1]
                    masterlist.append(ratio)
            line += 1

print(masterlist)
print(sum(masterlist))