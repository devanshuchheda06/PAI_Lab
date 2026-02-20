# Understanding Indexing and Slicing in 1D Array
print ("\n===== Indexing and Slicing in 1D Array ==== \n\n")
import numpy as np
a = np.array ([10, 20, 30, 40, 50])

# Indexing 
print ("Indexing:\n\t->a[1]:", a[1])
print ("\t->Element in Array a at a[-1]:", a[-1])

'''
Slicing: array [start : stop : step]
'''
print ("\nSlicing:\n\t->a[1:3]:", a[1:3])
print ("\t->a[-3:-1]:", a[-3:-1])
print ("\t->a[1:2]:", a[1:2])
print ("\t->a[0:4:-2]:", a[0:4:-2])
print ("\t->a[::-1]", a[::-1])