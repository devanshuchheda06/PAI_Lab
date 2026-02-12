# Understanding Constructor

print ("\n==== Constructor -> Explicit calling ==== \n\n")
print ("==== Inputting and Displaying Faculty Data ==== \n\n")

class Faculty:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary
        
    def display(self):
        print ("\nName of the Faculty:",self.name)
        print ("Subject assigned:",self.subject)
        print ("Salary obtained (in INR):",self.salary)
    
    def greet(self):
        print ("\nThank you for providing the information! Have a great Day...",self.name)
        
    def salaryEvaluation(self):
        if self.salary >= 10000:
            print ("Status: Good")
        else:
            print ("Status: Bad")
        

f1 = Faculty("Devanshu Chheda", "PAI", 15000)
f1.display()
f1.salaryEvaluation()
f1.greet()
