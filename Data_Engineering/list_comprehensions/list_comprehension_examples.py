# This example highlights the first 30 cube numbers
cubes = [i * i * i for i in range(1, 31)]
print(cubes)

# Printing out the multiples of 11
multiples_of_11 = [i * 11 for i in range(1, 31)]
print(multiples_of_11)

# Searching through a list of names according to specifications
data210 = ["Joy", "Andre", "Jess", "Alan", "Luke", "Lilian", "Tom", "Edmund", "Megha", "Ewan", "Diana", "Robert",
           "Lilian", "Akanksha", "Ethan", "Harry"]
j_data210 = [name for name in data210 if name.startswith("J")]
print(j_data210)


# Using a lambda function to do the next list comprehension (thanks Andre, Edmund, Tom, and Ethan)
def myfunc(n):
    return lambda a: a * n


six_percent_raise = myfunc(1.06)

# Using scalar multiplication of vectors to update salaries of employees
salaries = [45000, 53252, 67106, 44623, 25097, 87321, 131533]
salary_raises = [six_percent_raise(i) for i in salaries]
print(salary_raises)
