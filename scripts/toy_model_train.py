import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

test_split = 0.2

X_train, X_test, y_train, y_test = train_test_split(
    df[iris.feature_names],
    iris.target,
    test_size=test_split,
    stratify=iris.target,
)

n_trees = 100
clf = RandomForestClassifier(
    n_estimators=n_trees,
    oob_score=True,
)

clf.fit(X_train, y_train)

predicted = clf.predict(X_test)
acc = accuracy_score(y_test, predicted)

print(
    "Out of bag score estimate: {0:.3f}\n"
    "Mean accuracy: {1:.3f}".format(clf.oob_score_, acc)
)

model_save_path = "./models/toy-model.pkl"
with open(model_save_path, "wb") as file:
    pickle.dump(clf, file)
