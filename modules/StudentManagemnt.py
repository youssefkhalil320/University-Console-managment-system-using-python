from Student import  Student
from Worker import  Worker

OurStudents = []

def add_student(student):
    global OurStudents
    OurStudents.append(student)

def find_student_by_name(name):
    global OurStudents
    for student in OurStudents:
        if student.getName() == name:
            return student.description()

def find_student_by_id(sid):
    global OurStudents
    for student in OurStudents:
        if student.getId() == sid:
            return student.description()       


def sort_student_by_name():
    global OurStudents
    OurStudents = sorted(OurStudents, key = lambda x:x.name) 

def sort_student_by_id():
    global OurStudents
    OurStudents = sorted(OurStudents, key = lambda x:x.id)        
