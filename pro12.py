#Understanding reading a file
f1 = open ("text1", "r")
print (f1.read)
f1.seek(0)
print (f"Again reading the same file: {f1.read()}")
f1.seek(0)
print (f"Again reading the same file: {f1.read()}")
f1.close ()

f1 = open ("text1", "w")
f1.write ("Good Morning")
f1.close ()

f1 = open ("text1", "a")
f1.write ("\nGood Evening")
f1.close ()

f2 = open ("text2", "w")
f1 = open ("text1", "r")

#for image
for data in f1:
    f2.write (data)
f1.close ()
f2.close ()

r1 = open ("Screenshot11.jpg", "w")
r1.seek (0)
for data in r1:
    r1.write(data)
