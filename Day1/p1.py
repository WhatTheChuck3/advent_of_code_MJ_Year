def get_calibration_value_p1(calibration_in):
    output = ''
    for i, v in enumerate(calibration_in):
        if v.isnumeric():
            output += v
            break
    
    for i, v in enumerate(calibration_in[: :-1]):
        if v.isnumeric():
            output += v
            break
    return output

def test_index_for_digits(calibration_string, index):
    for j in range(3,6):
        test_string = calibration_string[index:index+j]
        if test_string in digit_dict[j]:
            return digits_spelled.index(test_string) + 1
    
    return False

def test_index_for_digits_reverse(calibration_string, index):
    for j in range(3,6):
        test_string = calibration_string[index:index+j]
        if test_string in digit_dict_reverse[j]:
            return digits_spelled.index(test_string[: :-1]) + 1
    
    return False

def get_calibration_value_p2(calibration_in):
    output = ''
    for i, v in enumerate(calibration_in):
        if v.isnumeric():
            output += v
            break
        test_index_output = test_index_for_digits(calibration_in, i)
        if test_index_output:
            output += str(test_index_output)
            break
    
    for i, v in enumerate(calibration_in[: :-1]):
        if v.isnumeric():
            output += v
            break

        test_index_output = test_index_for_digits_reverse(calibration_in[: :-1], i)

        if test_index_output:
            output += str(test_index_output)
            break
    return output

digits_spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_dict = {}
digit_dict_reverse = {}
for i in range(3,6):
    digit_dict[i] = [d for d in digits_spelled if len(d) == i]
    digit_dict_reverse[i] = [d[: :-1] for d in digits_spelled if len(d) == i]

input = open('input_i.txt')
sum_p1 = 0 
sum_p2 = 0
for line in input.readlines():
    sum_p1 += int(get_calibration_value_p1(line))
    sum_p2 += int(get_calibration_value_p2(line))

input.close()

print('P1.1 Answer ' + str(sum_p1))
print('P1.2 Answer ' + str(sum_p2))


