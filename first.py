print("This is my first program")

##addition of two numbers taking input from the user
number1=int(input("Enter the first number"))
number2=int(input("enter the second number"))
result=(number1)*(number2)
print("the result is",result)
print()
###conditional statement
if (result>100):
    print("the result is greater than 100")
    print(" Please enter a bigger number")
else:
    print("the result is less than 100")

###please create a program where you will have 5 participants, take the feedback of the class from the users
###then calculate the average of the feedback and print the average of the feedback
###if it is greater than 3 , then it is good, else it is bad
index=1
feedback1=int(input("Enter the feedback of" + str(index) + "the  participant no "))
feedback2=int(input("Enter the feedback of the second participant"))
feedback3=int(input("Enter the feedback of the third participant"))
feedback4=int(input("Enter the feedback of the fourth participant"))
feedback5=int(input("Enter the feedback of the fifth participant"))
average=(feedback1+feedback2+feedback3+feedback4+feedback5)/5
print("The average feedback is",average)
###4-5 : Very good 3-4: Average Below 3 is bad 2: Replace the teacher
if(average>4):
    print("Very good")
else:
    if(average>3):
        print("Average feedback is  average")
    else:
        if(average>2):
            print("average feedback is bad")
        else:
            print("Replace the trainer")
###elif
if(average>4):
    print("Very good")
elif(average>3):
    print("Average feedback is  average")
elif(average>2):
    print("average feedback is bad")
else:
    print("replace the teacher")

####

