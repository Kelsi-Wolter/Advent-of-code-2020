text_file = open('questions.txt').read().split('\n\n')

# Part 1:
# total = 0
# for text in text_file:
#     text_set = set(text)
#     text_set.discard('\n')
#     set_length = len(text_set)
#     total += set_length

# print(total)


# part 2
# make each line a set, and use set math to figure out which
# letters are the same between each set
# count those letters and add to total 

whole_list = []
for text in text_file:
    set_list = text.split('\n')
    new_set_list = []
    for ans_str in set_list:
        ans_set = set(ans_str)
        new_set_list.append(ans_set)
    
    whole_list.append(new_set_list)


int_set_list = []
for li in whole_list:
    if len(li) > 1:
        prev_set = set()

        for li_set in li:
            set_int = li_set.intersection((prev_set))
            prev_set = li_set
        
    else:
        set_int = li[0]
       
    int_set_list.append(set_int)

total = 0
for int_set in int_set_list:
    set_len = len(int_set)
    total += set_len
    

print(total)
    
    