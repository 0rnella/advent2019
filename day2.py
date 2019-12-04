
input = open('./day2-input', 'r').read().split(',')

# Part 1

def int_transformer (st):
    return int(st)

def computer (program):
    program_nums = map(int_transformer, program)

    marker = 0

    while (marker >= 0 and marker < len(program_nums)):
        opcode = program_nums[marker]

        if (opcode == 99):
            marker = -1

        if (opcode == 1 or opcode == 2):

            index1 = program_nums[marker+1]
            index2 = program_nums[marker+2]
            target_index = program_nums[marker+3]

            if (opcode == 1):
                program_nums[target_index] = program_nums[index1] + program_nums[index2]
            
            if (opcode == 2):
                program_nums[target_index] = program_nums[index1] * program_nums[index2]

            marker += 4
    
    return program_nums

# print(computer(input))















# I am teaching my partner to code and this is what they 
# came up with to start to tackle part 2.

# def opcode_extractor(long_list):
#     total_length = len(long_list)
#     max_number = total_length // 4

#     short_list = []

#     index = 0
#     for x in range(max_number):
#         short_list.append(long_list[index])
#         index += 4

#     return short_list

# print(opcode_extractor(input))