def test_location(i, j, incoming_direction = [0,0]):
    location = str(i)+'|'+str(j)
    if location in tested_tiles:
        return pipes2[i][j]
    else:
        tested_tiles.append(str(i)+'|'+str(j))
        
    for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
        # print('For '+str(i)+','+str(j)+' testing '+str(dir))
        # check_tile = pipes2[i][j]
        if dir[0] * -1 == incoming_direction[0] and dir[1] * -1 == incoming_direction[1]:
            # print('Dont go this way')
            pass
        else:
            tile = test_dir(i, j, dir[0], dir[1])
            if tile != 'U':
                pipes2[i][j] = tile
                # print('Updated '+str(i)+','+str(j)+' to '+tile)
                return tile

    return 'U'

        
def test_dir(i,j,di,dj):
    if i+di < 0 or j+dj < 0:
        # print('Outside the Lines')
        return 'O'
    try:
        step = pipes2[i+di][j+dj]
    except IndexError:
        # print('Outside the Lines')
        if pipes2[i][j] != 'X':
            return 'O'

    if step != 'X':
        if step == 'O':
            return 'O'
        elif step == 'I':
            return 'I'
        elif step == 'U':
            return test_location(i+di, j+dj, [di, dj])
        else: 
            print('Strange symbol at '+str(i+di)+','+str(j+dj))
    return 'U'


def print_pipes(pipes):
    for pipe_row in pipes:
        print(''.join(pipe_row))

        
def get_direction(direction_in, tile):
    # print('Approached '+tile+' from '+str(direction))
    if direction_in[0] == 1:
        match tile:
            case '-':
                return [1,0]
            case 'J':
                return [0,1]
            case '7':
                return [0,-1]
            case _:
                print('ERROR')
    elif direction_in[0] == -1:
        match tile:
            case '-':
                return [-1,0]
            case 'L':
                return [0,1]
            case 'F':
                return [0,-1]
            case _:
                print('ERROR')
    elif direction_in[1] == 1:
        match tile:
            case '|':
                return [0,1]
            case '7':
                return [-1,0]
            case 'F':
                return [1,0]
            case _:
                print('ERROR')
    elif direction_in[1] == -1:
        match tile:
            case '|':
                return [0,-1]
            case 'J':
                return [-1,0]
            case 'L':
                return [1,0]
            case _:
                print('ERROR')


import numpy as np
import sys
input = open('input.txt')
sys.setrecursionlimit(5000)

pipes = []
for line in input.readlines():
    pipes.append(line.replace('\n',''))

for i in range(len(pipes)):
    try: 
        start_index = pipes[i].index('S')
        position = [i,start_index]
        print(pipes[i])
    except:
        pass



start_position = position.copy()
print(position)
direction = [0,1]
steps = 0

pipes2 = np.array([np.array(['U','U']*len(pipes[0])), np.array(['U']*(len(pipes[0])*2))])

for i in range(1,len(pipes)):
    pipes2 = np.append(pipes2, np.array([['U','U']*len(pipes[0])]), axis = 0)
    pipes2 = np.append(pipes2, np.array([['U']*(len(pipes[0])*2)]), axis = 0)

pipes2[position[0]*2][position[1]*2] = 'X'
# print_pipes(pipes2)
while position != start_position or steps == 0:
    pipes2[position[0]*2 + direction[1]*-1][position[1]*2 + direction[0]] = 'X'
    position = [position[0] + direction[1]*-1, position[1] +direction[0]]
    
    tile = pipes[position[0]][position[1]]
    
    pipes2[position[0]*2][position[1]*2] = 'X'
    direction = get_direction(direction, tile)

    steps+=1
print('p1 is '+str(steps/2))


for start_i in range(len(pipes2)):
    # print('Row '+str(start_i))
    # print_pipes(pipes2)
    for start_j in range(len(pipes2[0])):
        tile = pipes2[start_i][start_j]

        if tile == 'U':
            # print('Testing '+str(start_i)+','+str(start_j))
            tested_tiles = []
            out_tile = test_location(start_i, start_j)
            if out_tile == 'U':
                pipes2[start_i][start_j] = 'I'

final_pipes = []    
counter = 0
for h in range(len(pipes2)):
    final_pipes.append([])
    for k in range(len(pipes2[0])):
        if h%2 == 0 and k%2 == 0:
            tile = pipes2[h][k]
            final_pipes[h].append(tile)
            if tile == 'I':
                counter+=1


print_pipes(final_pipes)
print('p2 is '+str(counter))