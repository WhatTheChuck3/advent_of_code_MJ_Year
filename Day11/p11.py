import numpy as np

def print_image(img):
    for row in img:
        print(''.join(row))

multiplier = 1000000
image = open('input.txt').read().splitlines()
image = np.array([[*x] for x in image])

rows, cols = image.shape

# print(image)
empty_rows = []
for row in range(rows):
    if np.all(image[row]=="."):
        empty_rows.append(row)
empty_rows.reverse()
insert_row = np.array(['.']*cols)


empty_columns = []
for column in range(cols):
    if np.all(image[:,column] == '.'):
        empty_columns.append(column)
empty_columns.reverse()
insert_col = np.array([['.']*(rows+len(empty_rows)*multiplier)])


print_image(image)

row_galaxy_inds, col_galaxy_inds = np.asarray(image=='#').nonzero()
print(row_galaxy_inds)
print(col_galaxy_inds)
print(empty_rows)
print(empty_columns)
summer1 = 0
summer2 = 0
# summer3 = 0
for i in range(len(row_galaxy_inds)):
    for j in range(i+1, len(row_galaxy_inds)):
        row1 = row_galaxy_inds[i]
        col1 = col_galaxy_inds[i]
        row2 = row_galaxy_inds[j]
        col2 = col_galaxy_inds[j]

        count_empty_rows = sum(1 for x in empty_rows if x > min(row1,row2) and x < max(row1,row2))
        count_empty_cols = sum(1 for x in empty_columns if x > min(col1,col2) and x < max(col1,col2))

        distance = abs(row2-row1) + abs(col2-col1) + count_empty_cols + count_empty_rows
        distance2 = abs(row2-row1) + abs(col2-col1) + (count_empty_cols + count_empty_rows)*(multiplier-1)
        # print(str(row1)+','+str(col1)+' to '+str(row2)+','+str(col2)+' = '+str(distance2)+' with '+str(count_empty_rows)+' rows and '+str(count_empty_cols)+' cols')
        
        summer1 += distance 
        summer2 += distance2

print('p1 is '+str(summer1))
print('p2 is '+str(summer2))