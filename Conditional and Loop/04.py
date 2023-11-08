# Exercise 4: Write a program to print multiplication table of a given number


# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

num = 2

# for i in range(2, 22, num):
#     print(i)


for i in range(1, 11, 1):
    result = num * i
    print(result)