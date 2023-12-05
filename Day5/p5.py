#Idea is to create a lookup dict that will pass along next lookup + number
# Then iterate through that until output = 'location'

#Had to adjust from an array lookup to bounds logic because the numbers are so GD big

input = open('input.txt')

seeds = input.readline().replace('\n','').split(" ")[1:]
map_bool = False
map_dict  = {}

for line in input.readlines():
    row = line.replace('\n','')

    if len(line) == 1:
        if map_bool:
            map_dict[source] = {
                'destination' : destination,
                'map_arr' : destination_mapping_dict
                }
        map_bool = False

        #enter info into dict
    elif map_bool:
        map_coords = row.split(" ")
        destination_start = int(map_coords[0])
        source_start = int(map_coords[1])
        range_length = int(map_coords[2])
        destination_mapping_dict[str(source_start)+' | '+str(source_start+range_length-1)] = destination_start - source_start

    else:
        map_input = row.split(" ")[0].split("-to-")
        map_bool = True
        source = map_input[0]
        destination = map_input[1]
        destination_mapping_dict = {}
        # destination_arr = list(range(0,99999999999)) ##this is so lame

map_dict[source] = {
    'destination' : destination,
    'map_arr' : destination_mapping_dict
}

# print(map_dict)
# Now lookup through the mappings
def get_seed_output(seed, map_dict):
    thing = 'seed'
    # print('Seed: ' + str(seed))
    idx = int(seed)
    while thing != 'location':
        map_entry = map_dict[thing]
        thing = map_entry['destination']
        for key, value in map_entry['map_arr'].items():
            bounds = key.split(' | ')
            if idx >= int(bounds[0]) and idx <= int(bounds[1]):
                idx = idx + value
                break
    return idx

locations = []

for seed in seeds:
    location = get_seed_output(seed, map_dict)
        # print(thing + ' '+ str(idx))
    locations.append(location)
    # print(idx)

print(min(locations))

##PART 2: instead of reversing the whole thing, can I assume the critical path window is large enough
## So I dont have to search every value, and can instead test the feasible space at intervals
## And then once critical path found, do one last exhaustive search locally


p2_min = 999999999999999
min_seed = 0
min_bucket_size = 0
for j in range(0, len(seeds), 2):
    print('Testing seeds')
    start_seed = int(seeds[j])
    end_seed = int(seeds[j])+int(seeds[j+1])
    bucket_size = 431 ##This takes about 2 minutes to run
    buckets = int((end_seed-start_seed)/bucket_size)
    # buckets = 100000
    # bucket_size = int((end_seed-start_seed)/buckets)


    print('Testing seeds '+str(start_seed)+ ' to '+str(end_seed)+' via '+str(buckets)+' buckets of size '+str(bucket_size))
    for k in range(start_seed, end_seed, bucket_size):
        location = get_seed_output(k, map_dict)
        if (location < p2_min):
            p2_min = location
            min_seed = k
            min_bucket_size = bucket_size

print(str(p2_min) + ' on seed '+ str(min_seed)+ ' via sparse search')

for h in range(min_seed-min_bucket_size+1, min_seed+min_bucket_size -1 ):
    location = get_seed_output(h, map_dict)
    if (location < p2_min):
        p2_min = location
        min_seed = h
   
print(str(p2_min) + ' on seed '+ str(min_seed)+ ' post final search')
