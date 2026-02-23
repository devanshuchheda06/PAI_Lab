# Understanding Zeros, Ones, Arange and Linspace
import numpy as np
print ("\n===== Zeros, Ones, Arange and Linspace =====\n\n")

# Zeroes
a = np.zeros ((2, 3), dtype = "i")
print ("Zeros -> a:\n", a)

# Ones
b = np.ones ((3,3,3), dtype = "i")
print ("\n\nOnes -> b:\n", b)

# Arange
# np.arange (start, stop, step)
c = np.arange (1, 10, 2) # Start from 1, stop not included, skip no. multiples of 2
print ("\n\nArange -> c:\n", c)

#linspace
d = np.linspace (1, 10, 2) # Returns evenly spaced values as per the last value (2 here)
print ("\n\nLinspace -> d:\n", d)