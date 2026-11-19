# linear regression implementation
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# start coding or generate with Ai
df=sns.load_dataset("titanic")
print(df.head())
print(df.columns)
print(df.info())
df.drop(["deck","embark_town","alive","class","who","adult_male"],axis=1,inplace=True)
print(df.info())
df["age"].fillna(df["age"].mean(),inplace=True)
df.dropna(subset=["embarked"],inplace=True)
print(df.info())
#level incode
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
print(df.head())
df['sex']=le.fit_transform(df['sex'])
df['embarked']=le.fit_transform(df["embarked"])
print(df.head())
#true false ko hatane ke liye
df = pd.get_dummies(df, drop_first=True, dtype=int)
print(df.head())
#divided into x and y level
X = df.drop("survived", axis=1)
y = df["survived"]

# Handle missing values
X = X.fillna(X.median())
# train test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(x_train, y_train)

# Prediction
y_pred = model.predict(x_test)

print(y_pred) 
print(y_test)
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred  ))
print(df)
#knn
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test.reindex(columns=x_train.columns))
from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors= 5)
knn_model.fit(X_train_scaled,y_train)
y_pred_knn = knn_model.predict(X_test_scaled)
print(accuracy_score(y_test,y_pred_knn))
print(confusion_matrix(y_test,y_pred_knn))
print(classification_report(y_test,y_pred_knn))
from sklearn.naive_bayes import GaussianNB
model_NB = GaussianNB()
model_NB.fit(x_train,y_train)
y_pred_NB = model_NB.predict(x_test)
print(accuracy_score(y_test,y_pred_NB))
print(confusion_matrix(y_test,y_pred_NB))
print(classification_report(y_test,y_pred_NB))
#decision tree
from sklearn.tree import DecisionTreeClassifier


class model_DT(DecisionTreeClassifier):
    """Decision-tree classifier with a useful default configuration."""

    def __init__(self, random_state=42, max_depth=None):
        super().__init__(random_state=random_state, max_depth=max_depth)


model_DT = model_DT()
model_DT.fit(X_train_scaled, y_train)
y_pred_DT = model_DT.predict(X_test_scaled)
print(y_pred_DT)
print(accuracy_score(y_test, y_pred_DT))
print(confusion_matrix(y_test,y_pred_DT))
print(classification_report(y_test,y_pred_DT))
#svc
from sklearn.svm import SVC
model_svm = SVC(kernel = 'linear')
model_svm.fit(X_train_scaled, y_train)
y_pred_svc = model_svm.predict(X_test_scaled)
print(accuracy_score(y_test,y_pred_svc))
print(confusion_matrix(y_test,y_pred_svc))
print(classification_report(y_test,y_pred_svc))
print(df)
X = df.drop('survived',axis = 1)
y = df['survived']
#cross validation
from sklearn.model_selection import cross_val_score
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
scores = cross_val_score(model_svm, X_scaled, y, cv=5, scoring='accuracy')
print(scores)
print(scores.mean())