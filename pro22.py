# Understanding Feature Encoding - 1. Label Encoding

print ("\n===== Feature Encoding - Label Encoding ======\n\n")
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

performance = ["Poor", "Good", "Excellent", "Average"]
print ("Type:",type (performance))
le = LabelEncoder ()
le.fit (performance) # Learns parameter
le.transform (performance) # Applies transformation
le.fit_transform (performance) # Learns and Applies