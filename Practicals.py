
# Machine Learning Practicals - Python Code Snippets

## 1. Object-Oriented Programming, Exception Handling, and File Operations

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: {self.filename} not found")
        except Exception as e:
            print(f"Error: {e}")

    def write_file(self, content):
        try:
            with open(self.filename, 'w') as f:
                f.write(content)
            print("File written successfully")
        except Exception as e:
            print(f"Error: {e}")

# Usage
fm = FileManager('data.txt')
fm.write_file('Hello, World!')
print(fm.read_file())
```

---

## 2. Data Cleaning, Transformation, and Analysis (Pandas & NumPy)

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Data cleaning
df.dropna(inplace=True)  # Remove null values
df.drop_duplicates(inplace=True)  # Remove duplicates

# Data transformation
df['new_col'] = df['col1'] + df['col2']
df['normalized'] = (df['value'] - df['value'].mean()) / df['value'].std()

# Data analysis
print(df.describe())
print(df.corr())
```

---

## 3. Classification and Regression Models (Scikit-learn)

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Classification
clf = LogisticRegression()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Regression
reg = RandomForestRegressor(n_estimators=100)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred)}")
```

---

## 4. Clustering Techniques (K-Means and DBSCAN)

```python
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

# Visualization
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels)
plt.show()
```

---

## 5. Deploy ML Model using Flask

```python
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 6. Ensemble Methods (Random Forest, Gradient Boosting, Stacking)

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Gradient Boosting
gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
gb.fit(X_train, y_train)

# Stacking
base_learners = [
    ('rf', RandomForestClassifier(n_estimators=50)),
    ('gb', GradientBoostingClassifier(n_estimators=50))
]
stacking = StackingClassifier(estimators=base_learners, final_estimator=LogisticRegression())
stacking.fit(X_train, y_train)

print(f"Stacking Score: {stacking.score(X_test, y_test)}")
```

---

## 7. Feature Scaling, Encoding, and Selection

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Feature Encoding
le = LabelEncoder()
categorical_col = le.fit_transform(df['category'])

# Feature Selection
selector = SelectKBest(score_func=f_classif, k=5)
X_selected = selector.fit_transform(X_scaled, y)
selected_features = selector.get_support(indices=True)
```

---

## 8. Text Classification using RNNs

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

# Tokenize text
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
X = pad_sequences(sequences, maxlen=100)

# Build RNN model
model = Sequential([
    Embedding(5000, 128),
    LSTM(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=32)
```

---

## 9. Image Classification using CNN

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Data augmentation
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory('train/', target_size=(224, 224))

model.fit(train_generator, epochs=10)
```

---

## 10. Build and Train Simple Deep Learning Model

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam

# Build simple deep learning model
model = Sequential([
    Dense(128, activation='relu', input_shape=(input_dim,)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(64, activation='relu'),
    BatchNormalization(),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # or 'softmax' for multi-class
])

# Compile
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
```

---

## Quick Reference Commands

```python
# Data loading
import pandas as pd
df = pd.read_csv('data.csv')

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model evaluation
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Visualization
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()
```
