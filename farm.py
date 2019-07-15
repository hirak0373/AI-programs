#Object:You've got chickens (2 legs), cows (4 legs) and dogs (4 legs) on your farm. Return the total number of legs on your farm.
def animal(chickens, cows ,dog ):
    total = chickens * 2 + cows * 4 + dog * 4
    return total
print(animal(2,3,5))
print(animal(1,2,3))
print(animal(5,2,8))