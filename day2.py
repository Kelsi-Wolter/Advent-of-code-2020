password_file = open('passwords.txt').read()

passwords = password_file.split('\n')



# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc


# PC:
# function takes in string, slices string into separate parts at colon, strip leading white space on second part:
#     first part will contain number range and letter
#         split by space --> number range and letter 
#         split range by -, set min and max
#         set letter to letter
#     second part will contain the password
#         count instances of letter in password to see if it falls within the range


# RC:

def password_checker(password):
    valid = 0
    slice_1 = password.split(':')
    legend = slice_1[0]
    word = slice_1[1]

    legend_slice = legend.split()
    min_max_slice = legend_slice[0].split('-')
    min_count = int(min_max_slice[0])
    max_count = int(min_max_slice[1])
    letter = legend_slice[1]

    if letter in word:
        word_count = word.count(letter)
        if word_count >= min_count and word_count <= max_count:
            valid += 1

    return valid

answer_1 = 0 
for password in passwords:
    answer_1 += password_checker(password)

print(answer_1)

def password_checker_2(password):

    valid = 0
    slice_1 = password.split(':')
    legend = slice_1[0]
    word = slice_1[1].strip()

    legend_slice = legend.split()
    index_slice = legend_slice[0].split('-')
    index_1 = int(index_slice[0]) - 1
    index_2 = int(index_slice[1]) - 1
    letter = legend_slice[1]
    

    if word[index_1] == letter and word[index_2] != letter:
        valid += 1
        
    elif word[index_1] != letter and word[index_2] == letter:
        valid += 1
        

    return valid

answer_2 = 0
for password in passwords:
    answer_2 += password_checker_2(password)

print(f'Answer 2 is {answer_2}')