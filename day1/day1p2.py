import regex as re

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

file_path = 'day1.txt'

def find_first_and_last_numbers(input):
    
    running_list = []
    
    with open(file_path, 'r') as file:
        
        for line in file:
            
            numbers = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line, overlapped=True)
            
            first_number = numbers[0]
            last_number = numbers[-1]

            if first_number.isdigit():
                first_number
            else:
                first_number = str(first_number)
                first_number = word_to_number[first_number]
                
            if last_number.isdigit():
                last_number
            else:
                last_number = str(last_number)
                last_number = word_to_number[last_number]
                
            two_digit_number = int(str(first_number) + str(last_number))
            running_list.append(two_digit_number)

    print(running_list)
    Sum = sum(running_list)
    print(Sum)


find_first_and_last_numbers(file_path)