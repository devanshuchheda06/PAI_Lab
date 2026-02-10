# Understanding Class and Objects in Python

print ("\n=====  OOPs in Python  =====\n\n")

class Student:
    def data(self):
        self.name = input ("Enter your name: ")
        self.age = int (input ("Enter your age: "))
    def display(self):
        print ("\nEntered name:",(self.name))
        print ("Entered age:",(self.age))
        
s1 = Student()
s1.data()
s1.display()
