
file_path = 'day2.txt'

with open(file_path, 'r') as file:
        
    running_list = []
    
    for line in file:

        blue_list = []
        red_list = []
        green_list = []

        offset = line.rfind(":") + 2
        shrunk = line[offset:-1]
        x = shrunk.split("; ")

        print(shrunk)
        print(x)

        for draw in x:
            draw = str(draw)
            cubes = draw.rsplit(", ")
            for a in cubes:
                b = a.rsplit(" ")
                print(b)
                if b[1] == "blue" or b[1] == "blu":
                    blue_list.append(int(b[0]))
                    print(blue_list)
                elif b[1] == "red" or b[1] == "re":
                    red_list.append(int(b[0]))
                    print(red_list)
                else:
                    b[1] == "green" or b[1 == "gree"]
                    green_list.append(int(b[0]))
                    print(green_list)

        print(max(red_list))
        print(max(green_list))
        print(max(blue_list))

        power = int(max(blue_list)) * int(max(red_list)) * int(max(green_list))
        print(power)
        running_list.append(power)
        
    Sum = sum(running_list)
    print(Sum)