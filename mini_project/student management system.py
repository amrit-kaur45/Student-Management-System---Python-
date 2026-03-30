students=[]
rollno=0
def addStudent():
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    grade=input("Enter student grade: ")
    marks=float(input("Enter student's marks: "))
    stud={}
    stud["name"]=name
    stud["age"]=age
    stud["grade"]=grade
    stud["marks"]=marks
    global rollno
    rollno+=1
    stud["rollno"]=rollno
    students.append(stud)
    print(f"Student added to the record with roll number {rollno}")
    
def removeStudent():
    roll=int(input("Enter the rollno of the student you want to delete"))
    if not students:
        print("No students added yet!No student can be removed.")
        return
    else:
        for val in students:
            if val["rollno"]==roll:
                students.remove(val)
                print("Student removed successfully!")
                return
        print("Student not found")        
    

def updateInfo():
    if not students:
        print("No students added yet so no updation possible.")
    else:
        roll=int(input("Enter the rollno of the student you want to update"))
        for val in students:
            if val["rollno"]==roll:
                print("Enter new data field you want to update: choose: ")
                choice=int(input("1.name  2.age  3.grade  4.marks"))
                if choice==1:
                    n=input("Enter new name")
                    val["name"]=n
                if choice==2:
                    a=int(input("Enter new age"))
                    val["age"]=a
                if choice==3:
                    g=input("Enter new grade")
                    val["grade"]=g   
                if choice==4:
                    m=float(input("Enter new marks"))
                    val["marks"]=m 
                print("Updation successful!")   
                return
        print("Student not found!")    

def viewAllStudents():
    if not students: #to check if students list is empty
        print("No students have been added yet.Add one to start viewing!")
        return
    else:   
        for val in students:
            print("Rollno: ",val["rollno"])
            print("Name :",val["name"])
            print("Age: ",val["age"])
            print("Grade: ",val["grade"])
            print("Marks: ",val["marks"])
            print("--------------------------")
            
print("---menu---")
print("1.Add new student \n2.Remove a student  \n3.Update student information  \n4.View all students  \n5.Exit ")

while True:
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            addStudent()
        case 2:
            removeStudent()
        case 3:
            updateInfo()
        case 4:
            viewAllStudents()
        case 5:
            print("code exited!")
            break
        case _:
            print("invalid choice!")
    

        


        

