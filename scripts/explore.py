import matplotlib.pyplot as plt
import pandas as pd
import sys

########################################################################################################################
# Processing the data
dataset = pd.read_csv('../data/dataset_mood_smartphone.csv', header=0)
# Convert to usable datetime
dataset.time = pd.to_datetime(dataset['time'], format='%Y-%m-%d %H:%M:%S.%f')

patients = dataset.id.unique()
first_patient = dataset.ix[dataset['id'] == patients[7]].ix[dataset['variable'] == 'mood']
patient_dict = {patient: list() for patient in patients}

########################################################################################################################
# Explore How many times a day, a patient scores his/her mood
mood_per_day = list()
count_mood = 0
day = None
last_mood = 6
average_mood = list()
total_mood = list()
for patient in patients:
    # patient_data = dataset.ix[dataset['id'] == patient].ix[dataset['variable'] == 'mood']
    patient_data = dataset.ix[dataset['id'] == patients[3]].ix[dataset['variable'] == 'mood']
    for i, date in enumerate(patient_data.time):
        count_mood += 1
        average_mood.append(patient_data.iloc[i].value)
        if date.day != day:
            mood_per_day.append(last_mood - float(sum(average_mood))/len(average_mood))
            total_mood.append(float(sum(average_mood)) / len(average_mood))
            last_mood = float(sum(average_mood))/len(average_mood)
            average_mood = list()
        day = date.day
    plt.plot(range(53), mood_per_day)
    plt.plot(range(53), total_mood)
    plt.show()
    sys.exit()
    # print(mood_per_day)
    # mood_per_day = list()
########################################################################################################################
# Plot a patients mood against time
plt.plot(first_patient['time'], first_patient['value'])
plt.show()
########################################################################################################################
