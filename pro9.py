# Understanding Class and Objects

print ("\n==== Class with Objects -> Explicit calling ==== \n\n")
print ("==== Inputting and Displaying Faculty Data ==== \n\n")

class Faculty:
    def data (self):
        self.name = input ("Enter name of the Faculty: ")
        self.subject = input ("Enter the subject assigned: ")
        self.salary = int (input ("Enter the salary obtained (in INR): "))
        
    def display(self):
        print ("\nName of the Faculty:",self.name)
        print ("Subject assigned:",self.subject)
        print ("Salary obtained (in INR):",self.salary)
    
    def greet(self):
        print ("\nThank you for providing the information! Have a great Day...",self.name)
        
f1 = Faculty()
f1.data()
f1.display()
f1.greet()
