def fizzbuzz(num):
    if num % 3 == 0 and num % 5 != 0:
        print("fizz")
        return "fizz"

    if num % 3 != 0 and num % 5 == 0:
        print("buzz")
        return "buzz"

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        return "fizzbuzz"
