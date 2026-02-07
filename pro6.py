# if-else used in for loop

print ("\nif-else in for loop:\n\n")
n = int (input ("How many times you want to enter the no.?: "))
print ("\t -> Entered n:",n)
print ("\t -> Type of entered n:",type(n))

for i in range (n) :
    num = int (input ("\nEnter number: "))
    print ("\t -> Entered num:",num)
    print ("\t -> Type of entered num:",type(num))

    if num > 0 :
        print ("\t -> Entered no. is positive")
    else :
        print ("\t -> Entered no. is negative")