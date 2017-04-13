import matplotlib.pyplot as plt
from sklearn import linear_model


class Explore:
    def __init__(self):
        self.x = None
        self.y = None

    def load_values(self, x, y):
        self.x = x
        self.y = y

    def scatterplot(self, color=None):
        plt.scatter(self.x, self.y, c=color)
        plt.show()
