import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

iris = load_iris()
print(iris["DESCR"])

df = pd.DataFrame(iris["data"], columns=iris["feature_names"])
df["target"] = iris["target"]

X = df.drop("target", axis=1)
y = df["target"]

def correlation (dataset, threshold):
    col_corr= set()
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
              colname = corr_matrix.columns [i]
              col_corr.add(colname)

    return col_corr

X = X.drop(correlation(X, 0.9), axis = 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

model = DecisionTreeClassifier(max_depth = 3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_train = model.predict(X_train)
accuracy_score(y_test, y_pred)

report = classification_report(y_test, y_pred, target_names = iris.target_names)

print("Model Accuracy: {accuracy}")
print("Classification Report:")
print(report)

