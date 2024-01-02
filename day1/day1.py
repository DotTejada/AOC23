import re

file_path = 'day1.txt'

def find_first_and_last_numbers(input):
    
    running_list = []
    
    with open(file_path, 'r') as file:
        
        for line in file:
            
            # Convert the strings to integers
            numbers = re.findall(r'\d', line)

            # Find the first and last numbers
            
            first_number = numbers[0]
            last_number = numbers[-1]
            two_digit_number = int(str(first_number) + str(last_number))
            running_list.append(two_digit_number)
        
    Sum = sum(running_list)
    print(Sum)


find_first_and_last_numbers(file_path)