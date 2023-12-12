input = open('input.txt').read().splitlines()
summer1 = 0
summer2 = 0

def get_combs(spring, counts, spring_ind, count_ind):
    map = {}

    def check_comb(spring_ind, count_ind, spring, counts):
        # print(str(spring_ind)+','+str(count_ind)+' '+counts)
        if (spring_ind, count_ind, counts) in map:
            return map[(spring_ind, count_ind, counts)]

        ## Check for case where it works through one of either whole string
        if spring_ind == len(spring) and count_ind == len(counts):
            # print('That works')
            return 1
        elif count_ind == len(counts):
            return 0
        elif spring_ind == len(spring):
            if counts[count_ind] == 'W':
                return check_comb(spring_ind, count_ind + 1, spring, counts)
            return 0

        ## Otherwise work through the string
        else:
            res = 0
            #They match, or assigned ? to # so they do, then proceed
            if (spring[spring_ind] == '#' or spring[spring_ind] == '?') and counts[count_ind] == '#':
                res += check_comb(spring_ind + 1, count_ind + 1, spring, counts)

            #W are wild(can be any sequence of ? or .), so add a . and check (add 1 to i) or move on (skip the *, add 1 to j)    
            elif (spring[spring_ind] == '?' or spring[spring_ind] == '.') and counts[count_ind] == 'W':
                res += check_comb(spring_ind + 1, count_ind, spring, counts)
                res += check_comb(spring_ind, count_ind + 1, spring, counts)

            ## cant be matched by # (as its on the ends), so just skip ahead
            elif spring[spring_ind] == '#' and counts[count_ind] == 'W':
                res += check_comb(spring_ind, count_ind + 1, spring, counts)

            # replace the + with a *, and then check the next spring    
            elif (spring[spring_ind] == '?' or spring[spring_ind] == '.') and counts[count_ind] == '+':
                res += check_comb(spring_ind + 1, count_ind, spring, counts[:count_ind] + 'W' + counts[count_ind + 1:])
        map[(spring_ind, count_ind, counts)] = res
        return res
    
    return check_comb(spring_ind, count_ind, spring, counts)    


for row in input:
    data = row.split()
    springs = data[0]
    springs2 = '?'.join([''.join(springs)]*5)
    counts = 'W'+'+'.join(['#' * int(n) for n in data[1].split(',')])+'W'
    counts2 = 'W'+'+'.join(['#' * int(n) for n in data[1].split(',')]*5)+'W'
    # print(springs)
    # print(counts)
    # print(springs2)
    # print(counts2)
    row_count = get_combs(springs, counts, 0, 0)
    row_count2 = get_combs(springs2, counts2, 0, 0)
    # print(row_count2)
    summer1 += row_count
    summer2 += row_count2

print('p1 is '+ str(summer1))
print('p2 is '+ str(summer2))