input = open('input.txt')

for line in input.readlines():
    row = line.replace('\n','')
    data = row.split(':')
    label = data[0] 
    if label == 'Time':
        time = data[1].strip().split()
        time2 = int(data[1].replace(' ',''))
    elif label == 'Distance':
        distance = data[1].strip().split()
        distance2 = int(data[1].replace(' ',''))

start_speed = 0 #mm / ms
acceleration = 1 #mm / ms / ms

def get_distance(start_speed, acceleration, hold_time, total_time):
    return (total_time - hold_time) * (hold_time * acceleration + start_speed)

count_winners = []
for i in range(0, len(time)):

    count = 0
    race_time = int(time[i])
    for j in range(0, race_time):
        if get_distance(start_speed, acceleration, j, race_time) > int(distance[i]):
            count += 1

    count_winners.append(count)

mult = 1
for wins in count_winners:
    mult *= wins

print('P1 is '+str(mult))

## P2, probably need to find the bounds ugh
## I can do math!
### 234102711571236 = (38677673 - x) * (x)
## x^2 - 38677673x + 234102711571236 = 0
## everybody knosw (-b plus minus sqrt(b²-4ac)/(2a)

import math
answer1 = (38677673 + math.sqrt(38677673**2 - 4*1*234102711571236)) / 2
answer2 = (38677673 - math.sqrt(38677673**2 - 4*1*234102711571236)) / 2
print(answer1)
print(int(distance2)  - get_distance(start_speed, acceleration, answer1, 38677673))
print(answer2)
print(int(distance2) - get_distance(start_speed, acceleration, answer2, 38677673))
print(answer2- answer1)
# print(time2)
# print(distance2)

# We love analytical solutions
