# Understanding Feature Encoding - 2. One-Hot Encoding

print ("\n===== Feature Encoding - One-Hot Encoding =====\n\n")
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame ({
    "Name": ["A", "B", "C", "D", "E"],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Math": [85, 78, 92, 70, 60],
    "Science": [90, 80, 85, 75, 65],
    "English": [70, 65, 80, 60, 55],
    "Pass": [1, 1, 1, 0, 0]
})

# 1. Encode Gender
le = LabelEncoder ()
df ["Gender Encoded"] = le.fit_transform (df["Gender"])
print (df)

# 2. Feature Scaling (Math, Science, English)
scaler = MinMaxScaler ()
df [["Math Scaled", "Science Scaled", "English Scaled"]] = scaler.fit_transform (df [["Math", "Science", "English"]])
print ()
print (df)

# 3. Feature Selection (Select top 2 features)
# Features to consider (scaled + encoded)
X = df [["Gender Encoded", "Math Scaled", "Science Scaled", "English Scaled"]]
y = df ["Pass"]

# Select top 2 features
selector = SelectKBest (score_func = f_classif, k = 2)
X_new = selector.fit_transform (X, y)

selected_features = X.columns [selector.get_support ()]
print ()
print (selected_features)
print ("Selected Features:", list (selected_features))
print ("Transformed Data:\n", X_new)

new_dataframe = pd.DataFrame (X_new, columns = selected_features)
print ()
print (new_dataframe)