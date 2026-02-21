# Understanding Indexing and Slicing in 2D Array
print ("\n===== Indexing and Slicing in 2D Array ==== \n\n")
import numpy as np
b = np.array ([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Indexing
print ("Indexing:\n\t->b[1, 2]:", b[1, 2])
print ("\t->b[2, 2]:", b[2, 2])
print ("\t->b[1, 1]:", b[1, 1])
print ("\t->b[-1, -1]:", b[-1, -1])

# Slicing
print ("\nSlicing:\n->b[0:2, 1:3]:\n", b[0:2, 1:3])
print ("\n->b[1:2, 1:2]:\n", b[1:2, 1:2])

# Indexing + Slicing
print ("\nIndexing + Slicing:\n\t->b[1, 0:2]:", b[1, 0:2])