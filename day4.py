# read passports, look for 7 fields - may have cid 
# field which is optional, count number of valid passports

# PC:

# split by line break, then split by spaces, should have at least
# 7 items after split by spaces
# if yes, need to have byr, iyr, eyr, hgt, hcl, ecl, pid 
#     --> valid

text_file = open('passports.txt').read().split('\n')

print(text_file)