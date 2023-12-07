input = open('input.txt')


def parse_hand_type2(hand):
    # print(hand)
    unique_chars = list(set(hand))
    count_list = []
    wild_lists = []
    for char in unique_chars:
        count_list.append(hand.count(char))
        if 'J' in unique_chars:
            wild_hand = hand.replace('J',char)
            new_unique_chars = list(set(wild_hand))
            new_wild_list = []
            # print('Replacing ' +char+': '+wild_hand)
            for wchar in new_unique_chars:
                new_wild_list.append(wild_hand.count(wchar))
            wild_lists.append(sorted(new_wild_list, key = lambda x: x*-1))
    
    count_list = sorted(count_list, key = lambda x: x*-1)
    if len(wild_lists) > 0:
        # print(wild_lists)
        wild_lists.append(count_list)
        sorted_lists = sorted(wild_lists)
        best_hand = sorted_lists[len(sorted_lists)-1]
        # print('Best hand: '+ str(best_hand))
    else:
        best_hand = count_list


    return [count_list, best_hand]

def get_char_rank(char, version = 1):
    if char.isdigit():
        return int(char)
    else:
        match char:
            case 'T':
                return 10
            case 'J':
                if version == 1:
                    return 11
                elif version == 2:
                    return 1
            case 'Q':
                return 12
            case 'K':
                return 13
            case 'A':
                return 14
            case _:
                print('You suck at coding')
                return 9


hands = []
for line in input.readlines():
    data = line.split()

    # print(data)
    hand_type = parse_hand_type2(data[0])
    data.append(hand_type)
    for char in data[0]:
        data.append(get_char_rank(char, 1))
    for char in data[0]:
        data.append(get_char_rank(char, 2))
    # print(hand_type)
    # print(data)
    hands.append(data)

sorted_hands = sorted(hands, key=lambda x: (x[2][0],x[3],x[4],x[5],x[6],x[7]))
sorted_hands2 = sorted(hands, key=lambda x: (x[2][1],x[8],x[9],x[10],x[11],x[12]))
# print (sorted_hands)

summer1 = 0
for rank in range(len(sorted_hands)):
    # print(sorted_hands[rank][0]+ ' is '+str(sorted_hands[rank][2])+' rank '+ str(rank+ 1)+' and bid '+sorted_hands[rank][1]+' and '+str(sorted_hands[rank][3:]) + ' score of '+str((rank+1) * int(sorted_hands[rank][1])))
    summer1 += (rank+1) * int(sorted_hands[rank][1])

summer2 = 0
for rank2 in range(len(sorted_hands2)):
    # print(sorted_hands2[rank2][0]+ ' is '+str(sorted_hands2[rank2][2])+' rank '+ str(rank2+ 1)+' and bid '+sorted_hands2[rank2][1]+' and '+str(sorted_hands2[rank2][3:]) + ' score of '+str((rank2+1) * int(sorted_hands2[rank2][1])))
    summer2 += (rank2+1) * int(sorted_hands2[rank2][1])

print('p1 is '+str(summer1))
print('p2 is '+str(summer2))