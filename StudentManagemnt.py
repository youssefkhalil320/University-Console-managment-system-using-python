from modules.Student import  Student
from modules.Worker import  Worker

OurStudents = []

def add_student(student):
    OurStudents.append(student)

def find_student_by_name(name):
    for student in OurStudents:
        if student.getName() == name:
            return student.description()

def find_student_by_id(sid):
    for student in OurStudents:
        if student.getId() == sid:
            return student.description()       


def sort_student_by_name():
    OurStudents = sorted(OurStudents, key = lambda x:x.name) 

def sort_student_by_id():
    OurStudents = sorted(OurStudents, key = lambda x:x.id)        
