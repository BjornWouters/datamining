import pandas as pd
import matplotlib.pyplot as plt
import tensorflow.contrib.learn as skflow
# Different classifiers
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import log_loss

df = pd.read_csv('learning.csv')
features = [
    'activity',
    'screen',
    'circumplex.arousal',
    'circumplex.valence',
    'call',
    'sms',
    'appCat.social',
    'appCat.builtin',
    'appCat.communication',
    'mood'
]
X = df[features]
y = df["mood_change"]

# Classifier
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                     hidden_layer_sizes=(10, 2), random_state=1)
clf = tree.DecisionTreeRegressor()
clf.fit(X, y)

# Testing
scores = cross_val_score(clf, X, y, cv=3)
print(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

print(clf.predict([[0.0897002479153,74.6829153776,0.2,0.4,2.0,8.0,150.112866667,19.45115,34.4449785714,6.8]]))