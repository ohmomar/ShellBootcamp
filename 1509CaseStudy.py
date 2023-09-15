class Student:
    #Constructor
    def __init__(self, name, rollno, section, email, stream):
        self.name = name
        self.rollno = rollno
        self.section = section
        self.email = email
        self.stream = stream
        
    #Add student
    def add_student(self, nname, rrollno, ssection, eemail, sstream):
        ob=Student(nname, rrollno,ssection,eemail,sstream)
        lst.append(ob)
        
    #Display students
    def disp_student(self,ob):
        print("Name: ",ob.name)
        print("Roll Number: ",ob.rollno)
        print("Section: ",ob.section)
        print("Email: ",ob.email)
        print("Stream: ",ob.stream)
        print("\n")
        
    #Function to search the student
    def search_student(self,rname):
        k=0
        for i in range(lst.__len__()):
            if(lst[i].name==rname):
                print(lst[i].name)
                return i
            else:
                return k
            
    #Delete the student        
    def delete_student(self,rname):
        i=obj.search_student(rname)
        if i==-2:
            print("Student Not Found!!")
        else:
            del lst[i]
    
    #Update Student Name
    def update_student(self,rrname,ssname):
        i=obj.search_student(rrname)
        if i==-2:
            print("Student Not Found!!")
        else:
            rrname=ssname
            lst[i].name=rrname
        
lst=[]
obj=Student('',0,'','','')
print("1. Add a new student")
print("2. Display all students")
print("3. Search a student")
print("4. Delete a student")
print("5. Update a student name")
print("To exit enter any number")

while(1):
    inputd = int(input("Enter Your Choice: "))
    if inputd == 1:
        print("ENTER NEW STUDENT DETAILS")
        nname = input("Student Name: ")
        nrollno = input("Student Roll Number: ")
        nsec = input("Student Section: ")
        nemail = input("Student Email: ")
        nstream = input("Student Stream: ")
        obj.add_student(nname,nrollno,nsec,nemail,nstream)
    elif inputd == 2:
        print("LIST OF STUDENTS")
        for i in range(lst.__len__()):
            obj.disp_student(lst[i])
    elif inputd == 3:
        print("SEARCH STUDENT")
        sename = input("Enter student name to search:")
        ans = obj.search_student(sename)
        if ans!=-2:
            print("Student Found!!")
        else:
            print("Student Not Found!!")
    elif inputd == 4:
        print("DELETE STUDENT")
        delname = input("Enter student name to delete: ")
        obj.delete_student(delname)
    elif inputd == 5:
        print("UPDATE STUDENT")
        oldname = input("Enter student name to be updated: ")
        newname = input("Enter updated name of the student: ")
        obj.update_student(oldname,newname)
            
