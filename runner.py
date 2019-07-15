l = []
while True:
    print("press 1 to enter score in a list")
    print ("press 2 for exit")
    ch = input()
    if ch == "1":
        a = input("Enter score: ")
        l.append(a) 
    elif ch == "2":
        break
for c in l:
    temp = 0
    if temp < int(c):
        temp = c
for c in l:
    temp1 = 0
    if temp1 < int(c) and int(c) != temp:
        temp1 = c
print(temp1)
