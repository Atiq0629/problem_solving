# Exercise 5: Check if the first and last number of a list is the same


# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.



# Given:

#     numbers_x = [10, 20, 30, 40, 10]
#     numbers_y = [75, 65, 35, 75, 30]

# Expected Output:
#     Given list: [10, 20, 30, 40, 10]
#     result is True

#     numbers_y = [75, 65, 35, 75, 30]
#     result is False


def first_last_same(givenList):
  print("Given List", givenList)
  
  fist_no = givenList[0]
  last_no = givenList[-1]
  
  if fist_no == last_no:
    return True
  else:
    return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print('Result is', first_last_same(numbers_x))
print('Result is', first_last_same(numbers_y))
    

