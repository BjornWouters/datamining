import matplotlib.pyplot as plt
import pandas as pd
import sys

# Local datamining objects
from datamining.scripts.explore import Explore

dataset = pd.read_csv('../data/dataset_mood_smartphone.csv', header=0)
# Convert to usable datetime
dataset.time = pd.to_datetime(dataset['time'], format='%Y-%m-%d %H:%M:%S.%f')
patients = dataset.id.unique()
patient_dict = {patient: list() for patient in patients}
first_patient = dataset.ix[dataset['id'] == patients[0]].ix[dataset['variable'] == 'mood']

mood_per_day = list()
count_mood = 0
day = None
for patient in patients:
    patient_data = dataset.ix[dataset['id'] == patient].ix[dataset['variable'] == 'mood']
    for date in first_patient.time:
        count_mood += 1
        if date.day != day:
            mood_per_day.append(count_mood)
            count_mood = 0
        day = date.day
    print(mood_per_day)
    mood_per_day = list()

sys.exit()
# explore_data = Explore()
# explore_data.load_values(x=x, y=y)
# explore_data.scatterplot(color=classes)
plt.plot(first_patient['time'], first_patient['value'])
plt.show()
