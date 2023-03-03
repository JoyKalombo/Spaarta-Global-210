
filename='sample.txt'
#
# file = open (filename)
#
# text = file.read()
#
# print(text)
#
# # The code above is not the best practice. This is because we open a channel and we need to close it.
#
# file.close()

with open(filename) as file:
    print(file.read())
    # The with is called "context manager". This also closes the file afterwards (you don't need to write "file.close()").


filename='sample1.txt'
with open(filename) as file:
    print(file.read())

try:
    with open(filename) as file:
        print(file.read())

except FileNotFoundError
    # you can save the name of the file to a log file
    print("the file could not be read")
except: