import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
# Different tree classifiers
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier

from sklearn.model_selection import cross_val_score
from sklearn.metrics import log_loss

df = pd.read_csv('learning.csv')
features = ['activity', 'screen', 'mood']

X = df[features]
y = df["mood_change"]

# Classifier
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                     hidden_layer_sizes=(5, 2), random_state=1)
clf = RandomForestClassifier()

# Testing
scores = cross_val_score(clf, X, y, cv=3)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))