# Exercise 7: Return the count of a given substring from a string


# Write a program to find how many times substring “Emma” appears in the given string.

# Given:
# str_x = "Emma is good developer. Emma is a writer"

# Expected Output:
# Emma appeared 2 times


# str_x = "Emma is good developer. Emma is a writer"
# count_result = str_x.count("Emma")
# print(count_result)


# Another Way
def count_result(statement):
    print("given string: ", statement)
    count = 0
    for i in range(len(statement) -1):
        count += statement[i: i+4] == 'Emma'
    return count

count = count_result("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "Times")