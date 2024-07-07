from Student import  Student
from Worker import  Worker

OurWorkers = []

def add_worker(worker):
    OurWorkers.append(worker)

def find_worker_by_name(name):
    for worker in OurWorkers:
        if worker.getName() == name:
            return worker.description()
    return "Student not found"


def find_worker_by_id(sid):
    for woker in OurWorkers:
        if worker.getId() == sid:
            return worker.description() 
    return "Student not found"              


def sort_worker_by_name():
    OurWorkers = sorted(OurWorkers, key = lambda x:x.name) 

def sort_worker_by_id():
    OurWorkers = sorted(OurWorkers, key = lambda x:x.id)
