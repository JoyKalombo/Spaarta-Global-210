print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
print(x[:5])
# A1a:

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in range(len(x)):
    if x[i] % 2 == 0:
        print(x[i])

# A1b:



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for i in range(5):
    if x[i] % 2 == 0:
        print(x[i])

# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
newlist = []
for i in range(len(names)):
    newlist.append(names[i][0])
print(newlist)
# A2a:





print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
list_of_space_index = []
for i in range(len(names)):
    list_of_space_index.append(names[i].index(" "))
print(list_of_space_index)






print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
list_of_initials = []
for i in range(len(names)):
    list_of_initials.append(names[i][0] + names[i][names[i].index(" ") + 1])

print(list_of_initials)
# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for i in range(len(list_of_lists)):
    if len(list_of_lists[i]) == len(set(list_of_lists[i])):
        print(list_of_lists[i])

# -------------------------------------------------------------------------------------- #


print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
def choose_a_number(choseninteger):
    while choseninteger > 100:
        print(choseninteger)
        break
    else: print("enter a number greater than 100")

choose_a_number(10)


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
def choose_a_number(choseninteger):
    while choseninteger > 100:
        for i in range(2,choseninteger):
            if choseninteger % i == 0:
                print("not prime")
                break
            else: print("prime")
            break
        break
    else: print("enter a number greater than 100")

choose_a_number((101))