#PythonIfStatements(if elif else)
#Require a number value for variable called age
age=int(input("How old are you? "))
print(age)
if age> 18:
        Late= age - 18
        print(str.format("You should have registered {} years ago.",Late))
elif age==18:
    print("Your Account has been approved")
else:
    print("You need to be 18 in order to register an account")
#If age less then eighteen print you must be eighteen to register an account


print("What is 2+2?")
answer =int(input(""))
if answer  == 4:
    print("Correct")
else:
    print("Incorrect")

#If a program is agrue for an exact string value the default input will be a string

print("What programming language is named after monty python")
language=input("")
if language == "Python" or "python":
    print("Correct")
else:
    print("Incorrect")
w
