pattern_file = open('day3_pattern.txt').read().split('\n')

pattern = []
for line in pattern_file:
    line.strip('\n')
    pattern.append(line)



# PC:
# find characters at an interval and keep track of any # (trees)
#     start at index on first line
#     move to index + 3 and next line
#     if index + 3 > length of that line,
#     new index = index + 3 - length of line - 1 
# count the number of #'s 

# RC:

tree_list = []
current_spot = 0
start = 0


hill = len(pattern) - 1

while start <= hill:
    current_line = pattern[start]
    route = current_line[current_spot]
    tree_list.append(route)
    last_index_of_line = len(current_line) - 1
    current_spot += 1
    start += 2
    
    if current_spot > last_index_of_line:
        current_spot = current_spot - last_index_of_line - 1
    
trees = tree_list.count('#')
print(trees)