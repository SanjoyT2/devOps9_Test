from flask import Flask, request, jsonify
#createing s server
app = Flask(__name__)
students = [{"name": "Rahul", "feedback": 4}, 
            {"name": "Rohit", "feedback": 3}, 
            {"name": "Rohan", "feedback": 2},
            {"name": "Raj", "feedback": 1},
            {"name": "Ravi", "feedback": 5}]
@app.route('/')
def hello_world():
    return 'Hello, World!'
##adding a student "This is for the main changes"
##adding a student this is for main branch testing
@app.route('/addStudent', methods=['POST'])
def addStudent():
    ###request : 
    student=request.json
    students.append(student)
    return (students)

###put resqyest
@app.route('/updateStudent', methods=['PUT'])
def updateStudent(studentName):
    studentInput=request.json
    for student in students:
        if(student["name"]==studentInput["name"]):
            student["feedback"]=studentInput["feedback"]
    return (students)

app.run(port=5000)





