# Understanding copying the new element at specified location
print ("\n===== Copying the element by .copy ===== \n\n")
import numpy as np
a = np.array ([1, 2, 3])
b = a [0:3].copy ()
print ("a:\n", a)
print ("b:\n", b)

b[0] = 4
print ("a:\n", a)
print ("b:\n", b)