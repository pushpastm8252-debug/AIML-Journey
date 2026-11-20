
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from importlib import import_module
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
try:
    XGBClassifier = import_module('xgboost').XGBClassifier
except (ImportError, AttributeError):
    XGBClassifier = None

df = sns.load_dataset('iris')
print(df.head())   
X = df.drop('species', axis=1)
y = df['species']
le = LabelEncoder()
y_encoded = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)
base_learners = [
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('svc', SVC(probability=True, kernel='rbf', random_state=42)),
    ('lr', LogisticRegression(max_iter=1000))
]
meta_learner = LogisticRegression(max_iter=1000)
stacking_clf = StackingClassifier(
    estimators=base_learners,
    final_estimator=meta_learner,
    cv=5
)
print(stacking_clf.fit(X_train, y_train))
y_pred = stacking_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(
    n_estimators=100,     # number of trees
    max_depth=None,       # let trees grow fully
    random_state=42,

)
print(rf_model.fit(X_train,y_train))
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
ada_model = AdaBoostClassifier(n_estimators=100, random_state=42)
print(ada_model.fit(X_train,y_train))
y_pred = ada_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
print(gb_model.fit(X_train,y_train))
y_pred = gb_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

if XGBClassifier is not None:
    xgb_model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        eval_metric='mlogloss',
        random_state=42,
    )
    print(xgb_model.fit(X_train, y_train))
    y_pred = xgb_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)
else:
    print('XGBoost is not installed; skipping XGBClassifier.')