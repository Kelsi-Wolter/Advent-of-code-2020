# read passports, look for 7 fields - may have cid 
# field which is optional, count number of valid passports

# PC:

# split by line break, then split by spaces, should have at least
# 7 items after split by spaces
# if yes, need to have byr, iyr, eyr, hgt, hcl, ecl, pid 
#     --> valid

text_file = open('passports.txt').read().split('\n\n')

passport_dict = {}
all_passports = {}
passport_list = []

for passport in text_file:
    passport = passport.replace('\n', ' ').split(' ')
    passport_list.append(passport)

n = 0
for passport in passport_list:
    for field in passport:
        keys = field.split(':')
        passport_dict[keys[0]] = keys[1]
    
    all_passports[str(n)] = passport_dict
    n += 1
    passport_dict = {}

valid = 0
# print(all_passports)
for person in all_passports:
    # if 'byr' and 'iyr' and 'eyr' and 'hgt' and 'hcl' and 'ecl' and 'pid' in all_passports[person]:
    #     valid +=1

    number_of_keys = len(all_passports[person])
   
    
    if number_of_keys == 8:
        valid += 1
    elif 'cid' not in passport_dict and number_of_keys == 7:
        valid += 1
        print(all_passports[person], number_of_keys)
        
print(valid)

