from Student import  Student
from Worker import  Worker

OurWorkers = []

def add_worker(worker):
    global OurWorkers
    OurWorkers.append(worker)

def find_worker_by_name(name):
    global OurWorkers
    for worker in OurWorkers:
        if worker.getName() == name:
            return worker.description()
    return "Student not found"


def find_worker_by_id(sid):
    global OurWorkers
    for worker in OurWorkers:
        if worker.getId() == sid:
            return worker.description() 
    return "Student not found"              


def sort_worker_by_name():
    global OurWorkers
    OurWorkers = sorted(OurWorkers, key = lambda x:x.name) 

def sort_worker_by_id():
    global OurWorkers
    OurWorkers = sorted(OurWorkers, key = lambda x:x.id)
