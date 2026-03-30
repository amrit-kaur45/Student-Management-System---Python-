class Student:
    def __init__(self, roll_no, name, age, grade, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks
class StudentManager: #Data class = one item. Manager class = handles the collection of items.”
    def __init__(self):
        self.students=[]
        self.next_roll_no=1
        
    def add_student(self):
        name=input("Enter student name: ")
        age=int(input("Enter student age: "))
        if(age<0):
            print("Invalid age entered: ")
            age=int(input("Re-enter student age: "))
            
        grade=input("Enter student grade: ")
        marks=float(input("Enter student's marks: "))
        if(marks<0 or marks>100):
            print("Invalid marks entered.")
            marks=float(input("Re-enter student's marks: "))
            
        student=Student(self.next_roll_no,name,age,grade,marks) #similar to dictionary of information and appending dictionary to list
        self.students.append(student)
        self.next_roll_no+=1
        print("Student has been successfully added.")
        self.save_to_file()
        
    def view_all_students(self):
        if not self.students:
            print("No students have been added yet.")
            return
        else:
            for val in self.students:  #val is ONE student object”
                print(f"Roll no: {val.roll_no}")
                print(f"Name: {val.name}")
                print(f"Age: {val.age}")
                print(f"Grade: {val.grade}")
                print(f"Marks: {val.marks}")
                print("--------------------")
                
    def remove_student(self):
        if not self.students:
            print("No students have been added yet. No student available to remove.")
            return
        else:
            r=int(input("Enter the roll no of student you want to remove: "))
            for val in self.students:
                if(val.roll_no == r):
                    self.students.remove(val)
                    print("Student deleted successfully from the record.")
                    return
            else:
                print("Rollno not found.")
            self.save_to_file()   
            
    def update_info(self):
        if not self.students:
            print("No students have been added yet. No student information available to update.")
            return
        else:
            r=int(input("Enter the roll no of student you want to update: "))
            for val in self.students:
                if(val.roll_no == r):
                    choice=int(input("1.name  2.age  3.grade  4.marks"))
                    if choice==1:
                        n=input("Enter new name")
                        val.name=n
                    elif choice==2:
                        a=int(input("Enter new age"))
                        val.age=a
                    elif choice==3:
                        g=input("Enter new grade")
                        val.grade=g   
                    elif choice==4:
                        m=float(input("Enter new marks"))
                        val.marks=m 
                    else:
                        print("invalid choice entered.")
                    print("Updation successful!")   
                    return
            else:
                print("No such record found.")
            self.save_to_file()  
                
    def search_student(self):
        if not self.students:
            print("Empty student record.")
            return
        else:
            r=int(input("Enter the roll no of student you want to update: "))
            for val in self.students:
                if(val.roll_no == r):
                    print(f"Name: {val.name}")
                    print(f"Age: {val.age}")
                    print(f"Marks: {val.marks}")
                    print(f"Grade: {val.grade}")
            else:
                print("Rollno not found in record.")
       
    def load_from_file(self):
        try:
            f = open("students.txt", "r")
        except FileNotFoundError:
        # File doesn't exist yet, so start with empty list
            print("No existing student data found. Starting fresh.")
            return
        for line in f:
            line=line.strip()   #remove whitespaces and newline \n
            if line == "":
                continue
            word=line.split("|")  #split with separator "|" & word:list
            roll_no=int(word[0])   #type casting
            age=int(word[2])
            marks=float(word[4])
            S=Student(roll_no,word[1],age,word[3],marks)
            self.students.append(S)
        self.next_roll_no= roll_no+1  #update next_roll_no
        f.close()
        
    def save_to_file(self):    
        f=open("students.txt","w")
        for s in self.students:  #loop over students list which stores OBJECT so dot notation
            roll=str(s.roll_no)
            name=s.name
            age=str(s.age)
            grade=s.grade
            marks=str(s.marks)
            line=roll+"|"+name+"|"+age+"|"+grade+"|"+marks+"\n"  # +to concatenate
            f.write(line)
        f.close()    
         
         
        
            
manager=StudentManager()    
manager.load_from_file()

print("---menu---")
print("1.Add new student \n2.Remove a student  \n3.Update student information  \n4.View all students   \n5.Search student information \n6.Exit ")

while True:
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            manager.add_student()
        case 2:
            manager.remove_student()
        case 3:
            manager.update_info()
        case 4:
            manager.view_all_students()
        case 5:
            manager.search_student()
        case 6:
            print("code exited!")
            break
        case _:
            print("invalid choice!")    

        
        
    

        
    
    
    
        
    
    
        
