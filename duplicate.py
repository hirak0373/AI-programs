#Object: Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates). (SET built-in function is not allowed)
l = ["John", "Taylor", "John"]
k = []
for c in l:
    flag = False
    for d in k:
        if c == d:
            flag = True
    if flag == False:
        k.append(c)

print(k)
     