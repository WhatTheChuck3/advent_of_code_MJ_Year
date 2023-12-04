
def test_row(row):
    infeasible_bool = False
    data = row.split(" ", 2)
    game_num = data[1][:-1]
    pulls = data[2].split("; ")
    max_cubes =  {
        'red':0,
        'green':0,
        'blue':0
    }

    for pull in pulls:
        counts = pull.split(", ")
        for count in counts:
            count_results = count.split(" ")
            color = count_results[1]
            count_cubes = int(count_results[0])
            if cube_dict[color]  < count_cubes:
                infeasible_bool = True
            max_cubes[color] = max(max_cubes[color], count_cubes)

    power_of_max_cubes = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']        

    if not infeasible_bool:
        return [int(game_num), power_of_max_cubes]
    else:
        return [0, power_of_max_cubes]

input = open('input_2.txt')

cube_dict = {
    'red':12,
    'green':13,
    'blue':14
}
summer = 0
summer2 = 0

# test = 'Game 100: 4 red, 3 green, 4 blue; 8 green, 5 red, 2 blue; 1 red, 2 blue, 7 green; 3 blue, 8 green, 5 red'

for line in input.readlines():
    
    output = test_row(line.replace("\n",""))
    summer += output[0]
    summer2 += output[1]

print(summer)
print(summer2)

