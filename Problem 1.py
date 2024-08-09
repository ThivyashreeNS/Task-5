""" Problem 1: What is the expected output of the following Python code """


data = [10, 501, 22, 37, 100, 999, 87, 357]
result = filter(lambda x : x > 4, data)
print(list(result))

""" Logic: Using filter function, we filters the list elements which are 
           greater than 4"""

 # Expected Output: [10, 501, 22, 37, 100, 999, 87, 357]