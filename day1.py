expenses = open('expenses.txt').read().split('\n')

expense_report = []


for line in expenses:
    expense_report.append(line)

# Look at expense report, find two numbers that add up to 2020 and multiply them together, result the result

# PC:

# Loop through the list of numbers
# Subtract each number from 2020 and look for the remainder as a number in the list
# add each number in the rest of the list to the current number until something adds up to 2020
# make list into set so there's no repeating numbers

# RC:

report_set = set(expense_report)



for expense in report_set:

    remainder = str(2020 - int(expense))
    if remainder in report_set:
        answer = int(remainder) * int(expense)
        print(f'Part one answer is {answer}, the two expenses are {remainder} and {expense}')


for expense_1 in report_set:
    for expense_2 in report_set:
        for expense_3 in report_set:
            sum = int(expense_1) + int(expense_2) + int(expense_3)
            if sum == 2020:
                answer = int(expense_1) * int(expense_2) * int(expense_3)
                print(f'The answer for part 2 is: {answer}, the expenses were {expense_1}, {expense_2}, {expense_3}.')
                break

