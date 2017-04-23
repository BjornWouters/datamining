import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import sys
import datetime
from scipy.stats.stats import pearsonr
# local imports
from scripts.prediction import PredictMood

mood_predictor = PredictMood()
########################################################################################################################
# Processing the data
dataset = pd.read_csv('../data/dataset_mood_smartphone.csv', header=0)
# Convert to usable datetime
dataset.time = pd.to_datetime(dataset['time'], format='%Y-%m-%d')
patients = dataset.id.unique()
first_patient = dataset.ix[dataset['id'] == patients[0]].ix[dataset['variable'] == 'mood']
patient_dict = {patient: list() for patient in patients}

my_patient = 5

########################################################################################################################
# Explore the fluctuation of a patient
explore_fluctuation = False
if explore_fluctuation:
    mood_per_day = list()
    count_mood = 0
    day = None
    last_mood = None
    average_mood = list()
    total_mood = list()
    for patient in patients:
        # patient_data = dataset.ix[dataset['id'] == patient].ix[dataset['variable'] == 'mood']
        patient_data = dataset.ix[dataset['id'] == patients[0]].ix[dataset['variable'] == 'mood']
        for i, date in enumerate(patient_data.time):
            count_mood += 1
            average_mood.append(patient_data.iloc[i].value)
            if date.day != day:
                if not last_mood:
                    last_mood = float(sum(average_mood)) / len(average_mood)
                mood_per_day.append(last_mood - float(sum(average_mood)) / len(average_mood))
                total_mood.append(float(sum(average_mood)) / len(average_mood))
                last_mood = float(sum(average_mood)) / len(average_mood)
                average_mood = list()
            day = date.day
        plt.plot(range(53), mood_per_day)
        plt.show()
########################################################################################################################
# Calculate the fluctuation of a/each patient
calculate_fluctuation = True
if calculate_fluctuation:
    previous_mood = None
    day = None
    count_days = 0
    mood_list = list()
    positive_change = list()
    negative_change = list()
    mood_days = list()
    patient = dataset.ix[dataset['id'] == patients[my_patient]]
    mood = patient.ix[dataset['variable'] == 'mood']
    for i, timestamp in enumerate(mood.time):
        previous_mood = mood.iloc[i].value
        if timestamp.day == day:
            mood_list.append(mood.iloc[i].value)
        else:
            if not day:
                day = timestamp.day
                mood_list.append(mood.iloc[i].value)
                continue
            if not previous_mood:
                previous_mood = np.mean(mood_list)
            else:
                mood_days.append((day, timestamp.month))
                change = previous_mood - np.mean(mood_list)
                previous_mood = np.mean(mood_list)
                mood_list = list()
                if change < 0:
                    negative_change.append(change)
                elif change > 0:
                    positive_change.append(change)
            count_days += 1

        day = timestamp.day

    pos_change_prob = len(positive_change) / count_days
    neg_change_prob = len(negative_change) / count_days
    pos_median = np.median(positive_change)
    neg_median = np.median(negative_change)
    mood_predictor.set_mood_fluctuation(positive=pos_change_prob, negative=neg_change_prob,
                                        pos_median=pos_median, neg_median=neg_median)
    mood_predictor.set_daily_mood(mood)
########################################################################################################################
# Find correlated attributes
find_attributes = True
if find_attributes:
    all_attributes = [
        'activity',
        'screen',
        'circumplex.arousal',
        'circumplex.valence',
        'call',
        'sms',
        'appCat.social',
        'appCat.builtin',
        'appCat.communication',
    ]
    for variable in all_attributes:
        variable = variable
        attribute = dataset.ix[dataset['id'] == patients[my_patient]].ix[dataset['variable'] == variable]
        if variable == 'call':
            print(attribute)
        total_attribute = list()
        previous_day = None
        attribute_list = list()
        count_day = 0
        for i, timestamp in enumerate(mood_days):
            myDate_1 = "2014-{}-{}".format(
                timestamp[1],
                timestamp[0]
            )
            myDate_2 = "2014-{}-{!s}".format(
                timestamp[1],
                timestamp[0]+1
            )

            try:
                result = attribute.loc[attribute.time >= myDate_1].loc[attribute.time < myDate_2]
            except ValueError:
                myDate_1 = "2014-{}-{!s}".format(
                    timestamp[1],
                    timestamp[0]-1
                )
                myDate_2 = "2014-{!s}-{}".format(
                    timestamp[1]+1,
                    '01'
                )

                result = attribute.loc[attribute.time >= myDate_1].loc[attribute.time < myDate_2]

            if not result.empty:
                    if variable not in ['sms', 'call']:
                        current_attribute = result.value.mean()
                    else:
                        current_attribute = result.value.sum()
                    total_attribute.append(current_attribute)
            else:
                total_attribute.append(0)
        print(pearsonr(mood_predictor.get_mood_per_day(), total_attribute))
        # plt.plot(range(len(total_attribute)), total_attribute, label='activity')
        # plt.show()
        mood_predictor.set_attribute(variable, total_attribute)
########################################################################################################################
# Create learning file
create_learning_file = True
if create_learning_file:
    with open('learning.csv', 'w') as output:
        writer = csv.writer(output, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        main_attributes = ['mood', 'mood_change']
        writer.writerow(all_attributes + main_attributes)

        mood_list = mood_predictor.get_mood_per_day()
        attributes = mood_predictor.get_attributes()
        for i, mood in enumerate(mood_list):
            if i != len(mood_list)-1:
                next_mood = mood_list[i+1]
                change = next_mood - mood
                if change == 0:
                    mood_change = 'same'
                elif change > 0:
                    mood_change = 'better'
                else:
                    mood_change = 'worse'

                values = list()
                for variable in all_attributes:
                    attribute = mood_predictor.get_attributes()[variable]
                    current_attribute = attribute[i]
                    values.append(current_attribute)

                writer.writerow(values + [mood, change])
########################################################################################################################
search_features = False
if search_features:
    activity = dataset.ix[dataset['id'] == patients[0]].ix[dataset['variable'] == 'activity']
    print(activity)
########################################################################################################################
# Plot a patients mood against time
# plt.plot(first_patient['time'], first_patient['value'])
# plt.show()
########################################################################################################################
# mood_predictor.predict_next_mood()
