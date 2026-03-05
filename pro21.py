# Understanding Feature Scaling - 2. Normalization

print ("\n===== Feature Scaling - Normalization =====\n\n")
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame ({
    "Income": [15000, 18000, 20000, 22000, 25000, 30000, 100000]
})

# Initialize Scaler
scaler = MinMaxScaler ()

# Apply scaling
df ["Scaled Income"] = scaler.fit_transform (df [["Income"]])

print (df)