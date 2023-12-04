def get_symbol_presence(data, row_index, starting_index, ending_index, number):
    symbol_bool = False
    row_len = len(data[row_index])

    start_i = max(0, row_index-1)
    end_i = min(len(data) -1, row_index+1)

    start_j = max(0, starting_index -1)
    end_j = min(ending_index+1,row_len-1)
    
    # print(str(start_i)+' | '+str(end_i)+' | '+str(start_j)+' | '+str(end_j))
    for h in range(start_i, end_i + 1):
        for k in range(start_j, end_j+1):
            if data[h][k] in symbol_list:
                symbol_bool = True
                idx_gear = str(h)+'|'+str(k)
                if idx_gear in gear_dict.keys():

                    gear_dict[idx_gear].append(number)
                else:
                    gear_dict[idx_gear] = [number]

    return symbol_bool


input = open('input.txt')
symbol_list = []
data = []
summer = 0 
gear_dict = {}

for line in input.readlines():
    row_data = line.replace('\n','')
    data.append(row_data)
    for val in row_data:
        if val != "." and not val.isdigit() and val not in symbol_list:
            symbol_list.append(val)


for i in range(len(data)):
    digit_test = False
    for j in range(len(data[i])):
        if data[i][j].isdigit():
            if j == len(data[i])-1 and digit_test:
                number = data[i][starting_index:j+1]
                # print('Testing '+number)
                if get_symbol_presence(data, i, starting_index, j+1, number):
                    summer += int(number)
                    # print('Included '+ number)
            elif not digit_test:
                digit_test = True
                starting_index = j
        elif digit_test:
            digit_test = False
            ending_index = j-1
            number = data[i][starting_index:ending_index+1]
            # print('Testing '+number)
            if get_symbol_presence(data, i, starting_index, ending_index, number):
                summer += int(number)
                # print('Included '+ number)


summer2 = 0 
for key, value in gear_dict.items():
    if len(value) == 2:
        summer2 += int(value[0]) * int(value[1])

print('P1 is ', summer)
print('P2 is ', summer2)