# Exercise 6: Display numbers divisible by 5 from a list.


# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Expected Output:
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55


def divisable_by_five(givenList):

    print("Given list is", givenList)
    print("Divisible by 5: ")
    for result in givenList:
        if result % 5 == 0:
            print(result)


numbers_x = [10, 20, 33, 46, 55]

divisable_by_five(numbers_x)
