print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors_of(chosen_number):
    list_of_divisors = []
    for i in range(1, chosen_number + 1):
        if chosen_number % i == 0:
            list_of_divisors.append(i)
    print("the divisors of", chosen_number, "are", list_of_divisors)
    return list_of_divisors

print("\nQ1b\n")

# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_factor_of_the_other(a, b):
    if (a in divisors_of(b)) or (b in divisors_of(a)):
        print(True)
    else:
        print(False)


is_factor_of_the_other(9, 5)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def position_of_letter(chosen_letter):
    # print(alphabet.index(chosen_letter.lower()))
    return alphabet.index(chosen_letter.lower())


# position_of_letter("J")

print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def id_generator_from_name(selected_name):
    number_holder = ""

    for i in range(len(selected_name)):
        number_holder += str(position_of_letter(selected_name[i]))
        # print(position_of_letter(selected_name[i]), end="")
        # return position_of_letter(selected_name[i])

    # print(number_holder)
    return int(number_holder)


# id_generator_from_name("joy")

print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password_generator(choose_a_name):
    # storage_number = 0
    # for i in range(len(choose_a_name)):
    #     if alphabet.index(choose_a_name[i].lower()) % 10 == 0:
    #         storage_number = storage_number * 10 + position_of_letter(choose_a_name[i].lower())
    #         print(storage_number)
    #     elif (alphabet.index(choose_a_name[i].lower()) % 10 != 0) and (alphabet.index(choose_a_name[i].lower()) % 100 == 0):
    #         storage_number = storage_number * 100 + alphabet.index(choose_a_name[i])
    #         print(storage_number)
    #
    # print(storage_number)
    sum_of_digits = 0
    for i in range(len(str(id_generator_from_name(choose_a_name)))):
        sum_of_digits += int(str(id_generator_from_name(choose_a_name))[i])
        print(sum_of_digits)
    print(id_generator_from_name(choose_a_name) - sum_of_digits)
    return id_generator_from_name(choose_a_name) - sum_of_digits
    # print(id_generator_from_name(choose_a_name) - sum_of_digits)


# password_generator("ppp")

password_generator("Joy")
# --------------------------------------------------------------------------------------

print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# A3a:
def it_is_prime(potential_prime):
    if potential_prime <= 1:
        print(False)
        return False
    elif potential_prime == 2:
        print(True)
        return True
    elif potential_prime > 2:
        for k in range(2, potential_prime):
            if potential_prime % k == 0:
                print(False)
                return False
                break
    print("True")
    return True


it_is_prime(87)

print("\nQ3b\n")


# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def it_is_prime_improved(potential_prime):
    if potential_prime <= 1:
        print(False)
        return False
    elif potential_prime == 2:
        print(True)
        return True
    elif potential_prime > 2:
        for k in range(2, potential_prime):
            if potential_prime % k == 0:
                print(False)
                return False
                break
    else:
        for i in str(potential_prime):
            if ord(str(potential_prime[i])) < 48 or ord(str(potential_prime[i])) > 57:
                print("enter an integer value...")

    print("True")
    return True


it_is_prime_improved("g5")
# -------------------------------------------------------------------------------------- #
