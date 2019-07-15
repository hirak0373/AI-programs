# Object: Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

def chk(a,b):
    attempt = False
    if len(a) == len(b):
        attempt = True
    return attempt

a = input("Enter input 1: ")
b = input("Enter input 2: ")
print(chk(a,b))