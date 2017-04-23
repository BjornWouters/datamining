import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from datetime import time
import sys

########################################################################################################################
# Processing the data

dataset = pd.read_csv('../data/dataset_mood_smartphone.csv', dayfirst=True, header=0)
dataset.index = pd.to_datetime(dataset['time'], format='%Y-%m-%d %H:%M:%S.%f')
dataset['date'] = pd.DatetimeIndex(dataset.time).date
dataset['day'] = dataset.index.day
dataset['month'] = dataset.index.month
dataset['year'] = dataset.index.year
dataset['time1'] = dataset.index.time
# dataset = dataset.drop('Unnamed: 0', 1)
patients = dataset.id.unique()
patient_data = (
'mood', 'circumplex.arousal', 'circumplex.valence', 'activity', 'screen', 'call', 'sms', 'builtin', 'communication',
'entertainment', 'finance', 'game', 'office', 'other', 'social', 'travel', 'unknown', 'utilities', 'weather')

# test printing
# print(dataset.at_time(time(15, 0)).head(10))
# print(dataset.variable['2014-03-25'])

# dates where patients use the apps
dates = [["14-3-2014", "16-4-2014"], ["21-03-2014", "8-05-2014"], ["14-03-2014", "05-05-2014"],
         ["24-04-2014", "08-05-2014"], ["18-03-2014", "03-05-2014"],
         ["14-3-2014", "4-5-2014"], ["21-3-2014", "27-4-2014"], ["27-3-2014", "5-5-2014"], ["13-3-2014", "3-5-2014"],
         ["21-3-2014", "5-5-2014"],
         ["14-3-2014", "6-5-2014"], ["13-3-2014", "5-5-2014"], ["20-3-2014", "5-5-2014"], ["21-3-2014", "5-5-2014"],
         ["21-3-2014", "29-4-2014"],
         ["22-3-2014", "4-5-2014"], ["14-4-2014", "8-6-2014"], ["8-4-2014", "8-5-2014"], ["12-4-2014", "29-5-2014"],
         ["3-4-2014", "13-5-2014"],
         ["1-4-2014", "8-5-2014"], ["2-4-2014", "13-5-2014"], ["20-3-2014", "4-5-2014"], ["1-4-2014", "5-5-2014"],
         ["1-4-2014", "13-5-2014"], ["16-4-2014", "31-5-2014"], ["18-4-2014", "5-5-2014"]]
## last patient i duplicated (needs to be fixed wrong dates)

# store all patients data with removed missing data
patients_data = {}
for i in range(0, len(patients)):
    data = dataset.ix[dataset['id'] == patients[i]]
    patients_data[patients[i]] = data[dates[i][0]:dates[i][1]]

patients_features = {}
dummy = None
for x in patients:
    mood = patients_data[x].ix[patients_data[x]['variable'] == 'mood'].resample('D', how='mean')['value']
    arousal = patients_data[x].ix[patients_data[x]['variable'] == 'circumplex.arousal'].resample('D', how='mean')[
        'value']
    valence = patients_data[x].ix[patients_data[x]['variable'] == 'circumplex.valence'].resample('D', how='mean')[
        'value']
    activity = patients_data[x].ix[patients_data[x]['variable'] == 'activity'].resample('D', how='mean')['value']
    screen = patients_data[x].ix[patients_data[x]['variable'] == 'screen'].resample('D', how='mean')['value']
    call = patients_data[x].ix[patients_data[x]['variable'] == 'call'].resample('D', how='sum')['value']
    sms = patients_data[x].ix[patients_data[x]['variable'] == 'sms'].resample('D', how='sum')['value']
    builtin = patients_data[x].ix[patients_data[x]['variable'] == 'builtin'].resample('D', how='mean')['value']
    communication = patients_data[x].ix[patients_data[x]['variable'] == 'communication'].resample('D', how='mean')[
        'value']
    entertainment = patients_data[x].ix[patients_data[x]['variable'] == 'entertainment'].resample('D', how='mean')[
        'value']
    finance = patients_data[x].ix[patients_data[x]['variable'] == 'finance'].resample('D', how='mean')['value']
    game = patients_data[x].ix[patients_data[x]['variable'] == 'game'].resample('D', how='mean')['value']
    office = patients_data[x].ix[patients_data[x]['variable'] == 'office'].resample('D', how='mean')['value']
    other = patients_data[x].ix[patients_data[x]['variable'] == 'other'].resample('D', how='mean')['value']
    travel = patients_data[x].ix[patients_data[x]['variable'] == 'travel'].resample('D', how='mean')['value']
    unknown = patients_data[x].ix[patients_data[x]['variable'] == 'unknown'].resample('D', how='mean')['value']
    utilities = patients_data[x].ix[patients_data[x]['variable'] == 'utilities'].resample('D', how='mean')['value']
    weather = patients_data[x].ix[patients_data[x]['variable'] == 'weather'].resample('D', how='mean')['value']
    temp = {'mood': pd.Series(mood), 'arousal': pd.Series(arousal), 'valence': pd.Series(valence),
            'activity': pd.Series(activity),
            'screen': pd.Series(screen), 'call': pd.Series(call), 'sms': pd.Series(sms),
            'builtin': pd.Series(builtin).abs(),
            'communication': pd.Series(communication), 'entertainment': pd.Series(entertainment),
            'finance': pd.Series(finance),
            'game': pd.Series(game), 'office': pd.Series(office), 'other': pd.Series(other),
            'travel': pd.Series(travel),
            'unknown': pd.Series(game), 'utilities': pd.Series(office), 'weather': pd.Series(weather)}
    patients_features[x] = pd.DataFrame(temp)

# testing if the data is correct
# pat = 1
# plt.figure(0)
# plt.plot(patients_features[patients[pat]]['mood'],label='mood')
# plt.plot(patients_features[patients[pat]]['arousal'],label='arousal')
# plt.plot(patients_features[patients[pat]]['valence'],label='valence')
# plt.plot(10*patients_features[patients[pat]]['activity'],label='activity')
# plt.plot(0.1*patients_features[patients[pat]]['screen'],label='screen')
# plt.plot(0.3*patients_features[patients[pat]]['call'],label='call')
# plt.plot(patients_features[patients[pat]]['sms'],label='sms')
# plt.plot(patients_features[patients[pat]]['builtin'],label='builtin')
# plt.plot(patients_features[patients[pat]]['communication'],label='communication')
# plt.plot(patients_features[patients[pat]]['entertainment'],label='entertainment')
# plt.plot(patients_features[patients[pat]]['finance'],label='finance')
# plt.plot(0.3*patients_features[patients[pat]]['game'],label='game')
# plt.plot(patients_features[patients[pat]]['office'],label='office')
# plt.plot(patients_features[patients[pat]]['travel'],label='travel')
# plt.plot(patients_features[patients[pat]]['unknown'],label='unknown')
# plt.plot(patients_features[patients[pat]]['entertainment'],label='entertainment')
# plt.plot(patients_features[patients[pat]]['utilities'],label='utilities')
# plt.plot(patients_features[patients[pat]]['weather'],label='weather')
# plt.legend()
# plt.show()


# data = patients_features[patients[0]].dropna(axis=1, thresh=10)


# making the final trainingset
train = {}
for x in patients:
    data = patients_features[x]
    number_of_days = len(data['mood'])
    if number_of_days >= 2:
        # only include features with enough coverage
        data = data.dropna(axis=1, thresh=math.ceil(0.5 * number_of_days))


        #### HERE I TRY TO CONCATONATE MOOD rows(index=i+1) WITH DATA (index=i
        # print(data)
        # no_mood = data.ix[1:number_of_days-1, data.columns != 'mood']
        # mood = data.ix[2:number_of_days, 1]
        # print(mood)
        # new_data = pd.concat([mood,no_mood],axis=1)
        # new_data['mood'] = data['mood'][number_of_days-1]
        # print(new_data)
        # break
        # for i in range(number_of_days-2):
        #     pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
