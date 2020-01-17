#Emmanuel Roy
BLT=["Bacon","Lettuce","Tomato"]
#Display the third placeholder in blt
print(BLT[2])
#Display the second placeholder in blt
print(BLT[1])
#Display the thrid placeholder in blt
print(BLT[0])



#Lists can hold basically anything.
Stuff=[3,'P',"Python",0]
#Display the fourth placeholder in the list called stuff
print(Stuff[3])
#Display the third placeholder in stuff
print(Stuff[2])
#Display the second placeholder in stuff
print(Stuff[1])
#Display the thrid placeholder in stuff
print(Stuff[0])

#Loop are done with for or while
for ingredient in BLT:
    print(ingredient)
    
something = 0

while something <  6:
    print("something = {value}".format(value = something))
    something = something + 1
