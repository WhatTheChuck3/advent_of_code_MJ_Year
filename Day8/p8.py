
import math

input = open('input.txt')
first_line = input.readline().replace('\n','')
print('First line: '+first_line)
gap_line = input.readline()

a_node_list = []
z_node_list = []
node_dict = {}
max_steps = 1

for line in input.readlines():

    row = line.replace('\n','')
    data = row.split(' = ')
    if data[0][2] == 'A':
        a_node_list.append(data[0])
    elif data[0][2] == 'Z':
        z_node_list.append(data[0])
    map = data[1].replace('(','').replace(')','').split(', ')
    node_dict[data[0]] = {
        'L': map[0],
        'R':map[1]
    }
    # print(row)

# print(node_dict)
def get_steps(node, first_line, node_dict):
    counter = 0
    input_length = len(first_line)
    while node[-1] != 'Z':
        dir = first_line[counter % input_length]
        node = node_dict[node][dir]
        counter += 1
    return counter
    
print('p1 is '+ str(get_steps('AAA',first_line, node_dict)))

print(a_node_list)
print(len(a_node_list))
print(z_node_list)

for node in a_node_list:
    steps = get_steps(node,first_line, node_dict)
    max_steps = math.lcm(steps,max_steps)
    print(node+' is '+ str(steps))
    print('This can repeat because it arrives there at the end of the map: '+str(steps%len(first_line)))

print('p2 is '+str(max_steps))