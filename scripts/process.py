from sklearn.datasets import load_iris

# Local datamining objects
from datamining.scripts.explore import Explore

# Test dataset
dataset = load_iris()
x = dataset.data[:, 1]
y = dataset.data[:, 2]
classes = dataset.target

explore_data = Explore()
explore_data.load_values(x=x, y=y)
explore_data.scatterplot(color=classes)
