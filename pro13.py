# Understanding Type, Dimensions, Shape, Size, Data-type, Item-size, N-bytes
import numpy as np
print ("\n==== NumPy for Numerical Computations ====\n\n==== NumPy Arrays -> Type, Dimensions, Shape, Size, Data-type, Item-size, N-bytes ====\n\n==== Numerical Computations on 1D, 2D & 3D NumPy Arrays ====\n")

a = np.array ([1, 2, 3])
print ("1D NumPy Array a :\n\n",a)
print ("\n- Type of Array a - type (a) :", type (a))

b = np.array ([
    [1, 2, 3],
    [4, 5, 6],
])
print ("\n2D NumPy Array b : \n\n", b)
print ("\n- Type of Array b - type (b) :", type (a))

c = np.array ([
    [[1, 2, 3]], [[4, 5, 6]],
    [[7, 8, 9]], [[10, 11, 12]]
])
print ("\n3D NumPy Array c : \n\n", c)
print ("\n- Type of Array b - type (c) :", type (c))

# Dimensions - .ndim
print ("\n\nDimensions of listed Arrays :\n")
print ("- Dimensions of Array a - a.ndim :", a.ndim)
print ("- Dimensions of Array b - b.ndim :", b.ndim)
print ("- Dimensions of Array c - c.ndim :", c.ndim)

# Shape - .shape 
print ("\n\nShape of listed Arrays (Returns a tuple):\n")
print ("- Shape of Array a - a.shape :", a.shape)
print ("- Shape of Array b - b.shape :", b.shape)
print ("- Shape of Array c - c.shape :", c.shape)

# Size - .size
print ("\n\nSize of listed Arrays:\n")
print ("- Shape of Array a - a.size :", a.size)
print ("- Shape of Array b - b.size :", b.size)
print ("- Shape of Array c - c.size :", c.size)

# Data-Type - .dtype
print ("\n\nData-type of listed Arrays :\n")
print ("- Data-type of Array a - a.dtype :",b.dtype)
print ("- Data-type of Array b - b.dtype :",b.dtype)
print ("- Data-type of Array c - c.dtype :",c.dtype)

# Size of items - .itemsize
print ("\n\nSize of Items of listed Arrays :\n")
print ("- Size of items of Array a - a.itemsize :", a.itemsize)
print ("- Size of items of Array b - b.itemsize :", b.itemsize)
print ("- Size of items of Array c - c.itemsize :", c.itemsize)

# Bytes used by Array elements - .nbytes = arr.size * arr.itemsize
print ("\n\nBytes used by elements of listed Arrays (Returns arr.size * arr.itemsize) :\n")
print ("- Bytes used by elements of Array a - a.nbytes :",a.nbytes)
print ("- Bytes used by elements of Array b - b.nbytes :",b.nbytes)
print ("- Bytes used by elements of Array c - c.nbytes :",c.nbytes)