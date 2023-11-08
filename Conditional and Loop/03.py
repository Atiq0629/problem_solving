# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Expected Output:
#     Enter number 10
#     Sum is:  55

# Solution 1: Using for loop and range() function
sum = 0
user_input = int(input("Enter number: "))

for i in range(1, user_input + 1, 1):
    sum += i
print("\n")
print("Sum is: ", sum)


# Solution 2: Using the built-in function sum()
user_input = int(input("Enter number: "))
x = sum(range(1, user_input+1))
print("Sum is: ", x)
