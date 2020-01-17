#Emmanuel Roy
#Programmer have to make distinct choices in the case that a program is arguing for two solutions
print("What is 2+2?")
answer=int(input(""))
if answer == 4:
    print("Correct")
else:
    print("Incorrect")


print("What is 4-2")
answer1=int(input(""))
if answer1 == 2:
    print("Correct")
else:
    print("Incorrect")

if answer1==2 and answer==4:
    print("You got both qestions right!")
else:
    print("You made some poor decisions.")
