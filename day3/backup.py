import re

masterlist = []
array = []
symbols = []
symbolindex = []

pattern = r'(=|\/|-|\+|\*|%|\$|#|@|&)'

filename = "day3/day3.txt"

with open(filename, 'r') as f:
    for line in f.readlines():
        array.append(line.strip().split(' '))

def combine_numbers(numbers):
    combined_number = int(''.join(map(str, numbers)))
    
    return combined_number

def findsymbols(linenum):
    for count, ele in enumerate(array[linenum][0]):
        symbol = re.findall(pattern, ele)
        if symbol:
            symbol = str(symbol[0])
            symbols.append(symbol)
            symbolindex.append(count)
            
    return symbols, symbolindex
     
def findleftright(linenum):
    for index in symbolindex:
        
        lnum = []
        rnum = []
         
        increm = 1
        while increm < 4:
            if array[linenum][0][index - increm].isdigit():
                print("left number at", str(index - increm))
                lnum.append(array[linenum][0][index - increm])
                increm += 1
            else:
                break
        lnum = list(reversed(lnum))
        if lnum:
            lnum = combine_numbers(lnum)
            masterlist.append(lnum)
            print(lnum)
            
        increm = 1
        while increm < 4:
            if array[linenum][0][index + increm].isdigit():
                print("right number at", str(index + increm))
                rnum.append(array[linenum][0][index + increm])
                increm += 1
            else:
                break
        if rnum:
            rnum = combine_numbers(rnum)
            masterlist.append(rnum)
            print(rnum)
        increm = 1

def findup(linenum):
    for index in symbolindex:
        
        upleftnum = []
        uprightnum = []
         
        increm = 1
        #initial check up
        if array[linenum - 1][0][index].isdigit():
            print("up number at", str(index))
            temp = array[linenum - 1][0][index]
            #checks left
            while increm < 4:
                if array[linenum - 1][0][index - increm].isdigit():
                    print("left number at", str(index - increm))
                    upleftnum.insert(0, array[linenum - 1][0][index - increm])
                    increm += 1
                else:
                    break

            #checks right
            increm = 1
            while increm < 4:
                if array[linenum - 1][0][index + increm].isdigit():
                    print("right number at", str(index + increm))
                    uprightnum.append(array[linenum - 1][0][index + increm])
                    increm += 1
                else:
                    break
                
            if upleftnum and uprightnum:
                upleftnum.append(uprightnum[0])
                upleftnum.insert(1, temp)
                upleftnum = combine_numbers(upleftnum)
                masterlist.append(upleftnum)
                print(upleftnum)
                
            elif upleftnum:
                upleftnum.append(temp)
                upleftnum = combine_numbers(upleftnum)
                masterlist.append(upleftnum)
                print(upleftnum)
                
            elif uprightnum:
                uprightnum.insert(0, temp)
                uprightnum = combine_numbers(uprightnum)
                masterlist.append(uprightnum)
                print(uprightnum)

def finddown(linenum):
    for index in symbolindex:
        
        downleftnum = []
        downrightnum = []
         
        increm = 1
        #initial check down
        if array[linenum + 1][0][index].isdigit():
            print("down number at", str(index))
            temp = array[linenum + 1][0][index]
            
            #checks left
            while increm < 4:
                if array[linenum + 1][0][index - increm].isdigit():
                    print("left number at", str(index - increm))
                    downleftnum.insert(0, array[linenum + 1][0][index - increm])
                    increm += 1
                else:
                    break
                
            #checks right
            increm = 1
            while increm < 4:
                if array[linenum + 1][0][index + increm].isdigit():
                    print("right number at", str(index + increm))
                    downrightnum.append(array[linenum + 1][0][index + increm])
                    increm += 1
                else:
                    break
                
            if downleftnum and downrightnum:
                downleftnum.append(downrightnum[0])
                downleftnum.insert(1, temp)
                downleftnum = combine_numbers(downleftnum)
                masterlist.append(downleftnum)
                print(downleftnum)
                
            elif downleftnum:
                downleftnum.append(temp)
                downleftnum = combine_numbers(downleftnum)
                masterlist.append(downleftnum)
                print(downleftnum)
                
            elif downrightnum:
                downrightnum.insert(0, temp)
                downrightnum = combine_numbers(downrightnum)
                masterlist.append(downrightnum)
                print(downrightnum)
               
        else:
            #checks left
            while increm < 4:
                if array[linenum + 1][0][index - increm].isdigit():
                    print("downleft number at", str(index - increm))
                    downleftnum.insert(0, array[linenum + 1][0][index - increm])
                    increm += 1
                else:
                    break
                
            #checks right
            increm = 1
            while increm < 4:
                if array[linenum + 1][0][index + increm].isdigit():
                    print("downright number at", str(index + increm))
                    downrightnum.append(array[linenum + 1][0][index + increm])
                    increm += 1
                else:
                    break
                
            if downleftnum:
                downleftnum = combine_numbers(downleftnum)
                masterlist.append(downleftnum)
                print(downleftnum)
                
            elif downrightnum:
                downrightnum = combine_numbers(downrightnum)
                masterlist.append(downrightnum)
                print(downrightnum)
                

linenum = 2

findsymbols(linenum)
findleftright(linenum)
findup(linenum)
finddown(linenum)

print(array[linenum - 1][0])
print(array[linenum][0])
print(array[linenum + 1][0])


print(symbols)
print(symbolindex)

print(masterlist)
print(sum(masterlist))