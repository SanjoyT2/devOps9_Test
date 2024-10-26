studentCount=0
sum=0
names=[]
##names[0] and feedbacks[0] are connected
###if there is a mismatch in index
###then the program will not work
###one variable where I can have the name and the feedback together
###dictionary
###key value pair

feedbacks=[]
userFlag="Y"
##they are connected through index
##
while(userFlag=="Y"):
    studentCount=studentCount+1
    name=input("Enter the name of the student")
    names.append(name)
    feedback=int(input("Enter the feedback of the student one by one"))
    print("The feedback of the student is",feedback)
    userFlag=input("Do you want to continue? Enter Y or N")
    feedbacks.append(feedback)
    sum=sum+feedback
average=sum/5

if(average>4):
    print("Very good")
elif(average>3):
    print("Average feedback is  average")
elif(average>2):
    print("average feedback is bad")
else:
    print("replace the teacher")

print("#########Feedback of the students#########")
for index in range(0,len(names)):
    print("The name of the student is",names[index])
    print("The feedback of the student is",feedbacks[index])