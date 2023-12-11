input = open('input.txt')
readings = []

for row in input.readlines():
    readings.append(list(map(int,row.replace('\n','').split())))

summer1 = 0
summer2 = 0
for data in readings:
    diff_list = [data]
    diff_data = data
    while not all(v == 0 for v in diff_data):
        # print(diff_data)
        new_deltas = [diff_data[n]-diff_data[n-1] for n in range(1, len(diff_data))]
        diff_list.append(new_deltas)
        diff_data = new_deltas
        
    # print(diff_list)
    delta = 0
    delta2 = 0
    for i in range(1,len(diff_list)+1):
        # print(str(diff_list[-1*i]) +' '+ str(diff_list[-1*i][-1] + delta))
        delta += diff_list[-1*i][-1] 
        # print(str(diff_list[-1*i][0] - delta2)+' '+str(diff_list[-1*i]))
        delta2 = diff_list[-1*i][0] - delta2
    summer1 += delta
    summer2 += delta2
    # print(delta2)

print('p1 is '+str(summer1))
print('p2 is '+str(summer2))