input = open('input.txt')
summer = 0 
summer1 = 0 
copies = [1] * 1000
index = 0

for line in input.readlines():
    row = line.replace('\n','')
    split1 = row.split(':')
    split2 = split1[1].replace("  "," ").strip().split(" | ")

    winning_nums = split2[0].split(" ")
    nums = split2[1].split(" ")
    counter = 0
    for num in nums:
        if num in winning_nums:
            counter += 1
    
    if counter > 0:
        summer += 2**(counter - 1)
        for i in range(0, counter):
            copies[index + i + 1] = copies[index + i + 1] +  copies[index]

    summer1 += copies[index]
    index +=1
    

print('P1 is '+str(summer))
print('P2 is '+str(summer1))