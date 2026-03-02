# Understanding Feature Scaling - 1. Standardization
print ("\n===== Feature Scaling - Standardization =====\n\n")
import pandas as pd
from sklearn.preprocessing import StandardScaler # Implemented using StandardScaler from scikit-learn

df = pd.DataFrame ({
    "Age": [20, 25, 30],
    "Salary": [20000, 50000, 80000]
})

print ("Unstandardized DataFrame:\n", df)

scaler = StandardScaler ()
scaled_data = scaler.fit_transform (df) # Returns NumPy array (.fit_transform takes data frames)
scaled_df = pd.DataFrame (scaled_data, columns = df.columns)
print ("\nStandardized DataFrame:\n", scaled_df)