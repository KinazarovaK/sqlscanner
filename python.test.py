list_of_strings = input().split(',')
# 🚨 Do  not change the code above
 
numbers = [int(x) for x in list_of_strings]

# list comprehension to filter on even numbers
result = [num for num in numbers if num%2==0]

print(result)
