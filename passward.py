#Object:Create a function that validates a password to conform to the following rules

from collections import Counter 
import re

def checkpas(a):
    flag = False
    if (len(a)>=6) and (len(a)<=26):
        if re.search("[a-z]",a) :
            if  re.search("[A-Z]",a):
                if  re.search("[0-9]",a):
                          if  re.search("[.,{><}:;!$#@'%^&*()_-]",a):
                            flag = True
                                        
                    

    res = Counter(a) 
    for val in res.values():
        if int(val) > 2:
            flag = False 
    return flag
a = input("Enter passward: ")
if checkpas(a) == True:
    print("Valid")
else:
    print("Invalid")
