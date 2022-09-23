from Student import Student

class Worker(Student):
    def __init__(self, name = "Human", id = 0000, dbirth = "20-12-2000", nat = "EG", gender = "M" , salary = 5000 ,working_hours = 9, job_title = "DR."):
        Student.__init__(self, name = "Human", sid = 0000, dbirth = "20-12-2000", nat = "EG", gender = "M")
        self.salary = salary
        self.working_hours = working_hours
        self.job_title = job_title
        
    def setSalary(self, salary):
        self.salary = salary

    def setWorkingHours(self, working_hours):
        self.working_hours = working_hours

    def setJobTitle(self,job_title):
        self.job_title = job_title

    def getSalary(self):
        return self.salary

    def getWorkingHours(self):
        return self.working_hours

    def getJobTitle(self):
        return self.job_title  

    def description(self):
        return f"Student Name is: {sel.name} id: {self.id} Gender is {self.gender} his salary is {self.salary}"                                                            



