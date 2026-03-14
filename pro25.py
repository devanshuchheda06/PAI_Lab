import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

# Load dataset
diabetes = load_diabetes ()
X = diabetes.data
y = diabetes.target
df = pd.DataFrame (X, columns = diabetes.feature_names)
print (df.head())

# Split data
X_train, X_test, y_train, y_test = train_test_split (
    X, y, test_size = 0.3, random_state = 42
)

# Create model
model = LinearRegression ()

# Train model
model.fit (X_train, y_train)

# Predictions
y_pred = model.predict (X_test)

# Evaluation
mae = mean_absolute_error (y_test, y_pred)
mse = mean_squared_error (y_test, y_pred)
rmse = np.sqrt (mse)
r2 = r2_score (y_test, y_pred)

print ("MAE: ", mae)
print ("MSE: ", mse)
print ("RMSE: ", rmse)
print ("R2", r2)
scores = cross_val_score (model, X, y, cv = 5)
print ("Cross Validation Score:", scores.mean())
