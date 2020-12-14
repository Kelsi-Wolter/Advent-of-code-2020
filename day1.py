expenses = open('expenses.txt')

expense_report = expenses.read()


# Look at expense report, find two numbers that add up to 2020 and multiply them together, result the result

# PC:

# Loop through the list of numbers
# Subtract each number from 2020 and look for the remainder as a number in the list
# add each number in the rest of the list to the current number until something adds up to 2020
# make list into set so there's no repeating numbers

# RC:

report_set = set(expense_report)

for expense in report_set:
    remainder = 2020 - expense
    if remainder in report_set:
        answer = remainder * expense
        return answer, remainder, expense
