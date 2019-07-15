# Object: Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
from collections import Counter 
l =["C","A","B","B","A","C"]
def M_vote(l):
    temp = 0
    res = Counter(l)
    #print(res)
    for key,val in res.items():
        #print(key,val)
        c = val/2
        #print(val)
        if c > temp:
            temp = c
            temp1 = key
    
        elif c == temp:
            temp1 = "none"
    return temp1
print(M_vote(l))
