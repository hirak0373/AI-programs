# Find a leap year
def is_leap(y):
    leap = False
    if y % 4 == 0:
        leap = True 
    elif (y % 100 == 0) and (y % 400 == 0):
        leap = True


    return leap
y = int(input())
print(is_leap(y)) 