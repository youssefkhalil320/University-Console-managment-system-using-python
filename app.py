from StudentManagemnt import *
from WorkerManagement import *
import sys




def ManageStudents():
    print("Hello Welcome to Student manager")
    option =  input("1: add stundent , 2: find by name , 3: find by id , 4:sort by name , 5:sort by id , 6:exit")
    while option not in "1234567":
        option =  input("enter a valid number plase")
    else:
        if option == "1":
            name = input("Enter the student name")
            sid = int(input("Enter student id "))
            dbirth = input("Enter the student's date of birth")
            nat = input("Enter the student nationality")
            gender = input("the student gender")
            new_student = Student(name,sid,dbirth,nat,gender)
            add_student(new_student)
        elif option == "2":
            option = input("Enter the student name ")
            print(find_student_by_name(option))
        elif option == "3":
            option = input("Enter the student id ")
            print(find_student_by_name(option))
        elif option == "4":
            sort_student_by_name()
        elif option == "5":
            sort_student_by_id()
        elif option == "6": 
            return                 

def ManageWorker():
    print("Hello Welcome to Worker manager")
    option =  input("1: add Worker , 2: find by name , 3: find by name , 4:sort by name , 5:sort by id , 6:exit")
    while option not in "1234567":
        option =  ("enter a valid number plase")
    else:
        if option == "1":
            name = input("Enter the worker name")
            sid = int(input("Enter worker id "))
            dbirth = input("Enter the worker's date of birth")
            nat = input("Enter the worker's nationality")
            gender = input("the worker gender")
            salary = int(input("the worker salary"))
            new_worker = Worker(name,sid,dbirth,nat,gender,salary)
            add_worker(new_worker)
        elif option == "2":
            option = input("Enter the worker name ")
            print(find_worker_by_name(option))
        elif option == "3":
            option = input("Enter the worker id ")
            print(find_worker_by_name(option))
        elif option == "4":
            sort_worker_by_name()
        elif option == "5":
            sort_worker_by_id()
        elif option == "6": 
            return
#our_functions = {1:ManageStudents() , 2:ManageWorker() , 3:sys.exit()}

print("Hello Welcome to University managment application")
while True:
    choice = int(input("Hello enter <1> for StudentManagemnt, <2> for WorkerManagment, <3> to exit"))
    while choice not in [1,2,3]:
        choice = input("Hello enter <1> for StudentManagemnt, <2> for WorkerManagment, <3> to exit")
    else:
        if choice == 1:  
            ManageStudents()
        elif choice == 2:  
            ManageWorker()
        elif choice == 3:  
            break        
