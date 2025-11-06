# import pandas as pd
# import numpy as np

# from joblib import dump
# from sklearn.datasets import load_iris

# iris = load_iris()
# # print(iris["DESCR"])

# df = pd.DataFrame(iris["data"], columns=iris["feature_names"])
# df["target"] = iris["target"]

# X = df.drop("target", axis=1)
# y = df["target"]


# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# X_train.shape, X_test.shape, y_train.shape, y_test.shape

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, classification_report

# model = DecisionTreeClassifier(max_depth = 3)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# y_pred_train = model.predict(X_train)
# accuracy = accuracy_score(y_test, y_pred)

# report = classification_report(y_test, y_pred, target_names = iris.target_names)

# print(f"Model Accuracy: {accuracy}")
# print("Classification Report:")
# print(report)


# dump(model, 'iris_model.pkl')
# print("Model saved as iris_model.pkl")
 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
 
# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target
 
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
# Train a RandomForest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
 
# Evaluate the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)
 
print(f"Model Accuracy: {accuracy}")
print("Classification Report:")
print(report)
 
# Save the trained model to a file
joblib.dump(clf, "iris_model.pkl")

