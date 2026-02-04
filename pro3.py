# Understanding if-else and if-elif ladder

print ("\nif-else and if-elif ladder:\n\n")
a = int (input ("Enter value of a: "))
b = int (input ("Enter value of b: "))

if a > b :
    print ("\n\t-> a is greater than b")
elif b > a :
    print ("\n\t-> b is greater than a")
else :
    print ("\n\t-> a and b are equal...")
    
if a >= 90 :
    print ("\n\t-> Topper")
elif a >= 70 :
    print ("\n\t-> Good")
elif a >= 50 :
    print ("\n\t-> Average")
else :
    print ("\n\t-> Fail")
