""" Problem 2: Write a python code using lambda function to check every element in the list
               is an integer or a string"""

# List with various type of data elements
data = ["hi", 10, "hello", 30, 20.4, True, (1,2,3)]

# Using lambda fn in filter(), we are filtering the integer or string elements from the given list
# isinstance is to check if an element is an integer or a string
result = list(filter(lambda x: isinstance(x, (int, str)), data))
print(result)