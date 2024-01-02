mydict = {
    "red": 12,
    're': 12,
    "green": 13,
    "blue": 14
}

index = 0

file_path = 'day2.txt'

with open(file_path, 'r') as file:
        
    running_list = []
    
    for line in file:
        
        # for one game
        offset = line.rfind(":") + 2
        shrunk = line[offset:-1]
        x = shrunk.split("; ")

        print(shrunk)
        print(x)

        possible = True
        
        for draw in x:
            draw = str(draw)
            cubes = draw.rsplit(", ")
            #checking for possibilty
            for a in cubes:
                b = a.rsplit(" ")
                if int(b[0]) <= mydict[b[1]]:
                    print(possible)
                else:
                    possible = False
                    print(possible)
                    break
                
            if not possible:
                break
        
        index += 1
        if possible:
            running_list.append(index)
            
    Sum = sum(running_list)
    print(Sum)