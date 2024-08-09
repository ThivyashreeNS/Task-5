""" Problem 3: Using Python lambda function create a Fibonacci series from 1 to 50 elements"""

#  No. of Fibonacci elements.
count=50

# Initializes the list with the first two Fibonacci numbers.
fib_list = [0, 1]

# Applies a lambda function to each element in the range 2 to n - 1.
# This lambda function appends the sum of the last two elements of fib_list to fib_list.
# Here the '_' represents the variable in the lambda fun is unused.

fibonacci = list(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, count)))

print(fib_list)
