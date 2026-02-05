# Understanding if-else and if-elif ladder

print ("\nif-else and if-elif ladder:\n\n")
name = input ("Enter Student's Name: ")
print ("Entered Name:",(name))
print (type(name))
print ()

marks = int (input ("Enter Student's Marks: "))
print ("Entered Marks:",(marks))
print (type(marks))

if marks >= 75 :
    print ("\t -> Distinction")
elif marks >= 60 :
    print ("\t -> First Class")
elif marks >=40 :
    print ("\t -> Passed")
else :
    print ("\t -> Fail")