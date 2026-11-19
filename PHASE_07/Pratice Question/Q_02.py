import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('iris')
print(df.head())
df['species'].unique()
from sklearn.model_selection import train_test_split
X=df.drop('species',axis=1)
y=df['species']

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.33, random_state=42)

from sklearn.neighbors import KNeighborsClassifier
model_knn = KNeighborsClassifier(n_neighbors=13)
print(model_knn.fit(X_train,y_train))
model_knn.score(X_test,y_test)
from sklearn.svm import SVC
model_svm = SVC(gamma= 'auto')
print(model_svm.fit(X_train,y_train))
model_svm.score(X_test,y_test)

from sklearn.model_selection import GridSearchCV

classifier = GridSearchCV((model_svm),{
    'C' : [1,10,20,30],
    'kernel' :['rbf','linear'],
},cv = 5,return_train_score = False)
print(
classifier.fit(X,y))
print(
classifier.cv_results_)

results = pd.DataFrame(classifier.cv_results_)
print(
results)

results[['param_C','param_kernel','mean_test_score']]
from sklearn.model_selection import RandomizedSearchCV
classifier_r = RandomizedSearchCV((model_svm),{
    'C' : [1,10,20,30],
    'kernel' :['rbf','linear'],
},n_iter = 4,cv = 5,return_train_score = False)
print(
classifier_r.fit(X,y))

results = pd.DataFrame(classifier_r.cv_results_)
print(
results)

results[['param_C','param_kernel','mean_test_score']]