# Understanding Fancy Indexing & Boolean Masking
print ("\n===== Fancy Indexing and Boolean Masking =====\n\n")
import numpy as np

# Fancy Indexing
a = np.array ([10, 20, 30, 40, 50])
indices = [0, 2, 4]
b = a [indices]
print ("Fancy indexed -> b:", b)

# Boolean Masking
mask = (a > 20) & (a < 50)
print ("\nBoolean Masked:", mask)
c = a[mask]
print ("Masked Value of c:", c)