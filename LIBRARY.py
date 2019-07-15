#Your task is to write a computer program that asks the user if they are looking for a fiction or a non-fiction book. Based on the user answer the program will ask the user to choose the genre from a list of available genres. Finally the program will return the location (A to I) of books of this genre
available_genre1=["comedy","comic","science fiction","fantasy","historical fiction"]
available_genre2=["history and geography","arts","science and tchnology","other"]
print("If u r looking for fiction press 1")
print("If u r looking for non-fiction press 2")
ch1 = input("Enter ur choice: ")
def ss(ch):
    if ch == "1":
        print("Choose the genre from the list ",available_genre1)
        a = input()
        if a.lower() == "comedy":
            return "A"
        elif a.lower() == "comic":
            return "B"
        elif a.lower() == "science fiction":
            return "C"
        elif a.lower() == "fantasy":
            return "D"
        elif a.lower() == "historical fiction":
            return "E"
    elif ch == "2":
        print("Choose the genre from the list ",available_genre2 )
        a = input()
        if a.lower() == "history and geography":
            return "F"
        elif a.lower() == "arts":
            return "G"
        elif a.lower() == "science and tchnology":
            return "H"
        elif a.lower() == "other":
            return "I"
print(ss(ch1))    


