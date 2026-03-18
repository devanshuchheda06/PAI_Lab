# Understanding Decision Trees

#import required libraries
import pandas as pd
import numpy as np

#dataset
from sklearn.datasets import load_iris

#train test split
from sklearn.model_selection import train_test_split

#Decision Tree model
from sklearn.tree import DecisionTreeClassifier

#Evaluation metrics
from sklearn.metrics import accuracy_score

#Hyperparameter tuning
from sklearn.model_selection import GridSearchCV

#-------------------------------------------------------------------------------
# 1. Load Iris dataset
#-------------------------------------------------------------------------------

#load Iris Dataset
data = load_iris()

#feature (x) and Target (y)
X = data.data
Y = data.target

#-------------------------------------------------------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print("Training samples: ", X_train.shape[0])
print("Testing samples: ", X_test.shape[0])

#-------------------------------------------------------------------------------
# 3. Train Decision Tree (Overfitting Example)
#-------------------------------------------------------------------------------

#Create Decision tree with NO restrictions
model = DecisionTreeClassifier(random_state=42)

#Train the model
model.fit(X_train, Y_train)

#Prediction
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

#Accuracy
train_acc = accuracy_score(Y_train, train_pred)
test_acc = accuracy_score(Y_test, test_pred)

print("\n---------- Before Hyperparameter Tuning ---------")
print("Training Accuracy: ", train_acc)
print("Testing Accuracy: ", test_acc)

#If training accuracy is very high and testing accuracy is lower.
#it indicates OVERFITTING.

#-------------------------------------------------------------------------------
#4. Hyperparameter tuning (manual)
#-------------------------------------------------------------------------------

#Limit tree complexity
model_tuned = DecisionTreeClassifier(max_depth=2, min_samples_split=5, random_state=42)

#Train tuned model
model_tuned.fit(X_train, Y_train)

#Prediction
train_pred2 = model_tuned.predict(X_train)
test_pred2 = model_tuned.predict(X_test)

#Accuracy
train_acc2 = accuracy_score(Y_train, train_pred2)
test_acc2 = accuracy_score(Y_test, test_pred2)

print("\n------------ After manual Hyperparameter Tuning ------------")
print("Training Accuracy: ", train_acc2)
print("Testing Accuracy: ", test_acc2)

#-------------------------------------------------------------------------------
#5. Hyperparameter tuning using GridSearchCV
#define parameter grid
param_grid = {
  'max_depth': [2,3,4,5,6] ,
  'min_samples_split': [2,3,10],
  'min_samples_leaf': [1,2,4]
}

#Create base model
dt = DecisionTreeClassifier(random_state=42)

# GridSearchCV
grid = GridSearchCV(estimator=dt, param_grid=param_grid, cv=5, scoring='accuracy')

#train grid search
grid.fit(X_train, Y_train)

print("\nBest Parameters Found:", grid.best_params_)

#best model
best_model = grid.best_estimator_

#predictions
Y_pred = best_model.predict(X_test)

#final accuracy
final_acc = accuracy_score(Y_test, Y_pred)
print("Final Test Accuracy After GridSearchCV: ", final_acc)
