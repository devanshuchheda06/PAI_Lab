# Understanding creating, training and evaluating ML Models

print ("\n===== ML Model - Creation, Training, Predictions & Evaluations =====\n\n")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
iris = load_iris ()
X = iris.data
y = iris.target
df = pd.DataFrame (X, columns = iris.feature_names)
df ["species"] = iris.target
print (df.head()) # Prints 5 values by default among 150 from dataset
print ("Features Names: ", iris.feature_names)
print ("\nTarget Data: ", iris.target)
print ("\nTarget Names: ", iris.target_names)
# print ("X ----------->", X)
# Split data
X_train, X_test, y_train, y_test, = train_test_split (
    X, y, test_size = 0.3, random_state = 42
)

# Create model
model = LogisticRegression (max_iter = 200)

# Train model
model.fit (X_train, y_train)

# Predictions
y_pred = model.predict (X_test)

# Confusion matrix
cm = confusion_matrix (y_test, y_pred)

# Evaluation
print ("Accuracy: ", accuracy_score (y_test, y_pred))
print ("\nConfusion Matrix: \n", cm)
print ("\nClassification Report: \n", classification_report (y_test, y_pred))

print ("Train Score: ", model.score (X_train, y_train))
print ("Test Score:", model.score (X_test, y_test))
