import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

########################################################################################################################
# Processing the data
dataset = pd.read_csv('../data/dataset_mood_smartphone.csv', header=0)
# Convert to usable datetime
dataset.time = pd.to_datetime(dataset['time'], format='%Y-%m-%d %H:%M:%S.%f')
patients = dataset.id.unique()
first_patient = dataset.ix[dataset['id'] == patients[7]].ix[dataset['variable'] == 'appCat.weather']
patient_dict = {patient: list() for patient in patients}

########################################################################################################################
# Plot a patients against time
patientnumber = 8

mood = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'mood']
arousal = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'circumplex.arousal']
valence = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'circumplex.valence']
activity = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'activity']
screen = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'screen']
call = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'call']
sms = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'sms']
builtin = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.builtin']
communication = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.communication']
entertainment = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.entertainment']
finance = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.finance']
game = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.game']
office = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.office']
other = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.other']
social = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.social']
travel = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.travel']
unknown = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.unknown']
utilities = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.utilities']
weather = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == 'appCat.weather']

plt.figure(0)
plt.plot(mood['time'], 10*mood['value'],label='mood')
plt.plot(arousal['time'], 5*arousal['value'],label='arousal')
plt.plot(valence['time'], 5*valence['value'],label='valence')
plt.plot(activity['time'], 20*activity['value']+20,label='activity')
plt.plot(screen['time'], 20*screen['value']+20,label='screen')
plt.plot(call['time'], 20*call['value']+20,label='call')
plt.plot(sms['time'], 20*sms['value']+20,label='sms')
plt.plot(builtin['time'], .05*builtin['value']+20,label='builtin')
plt.plot(communication['time'], 0.1*communication['value']+10,label='communication')
plt.plot(entertainment['time'], 0.1*entertainment['value']+10,label='entertainment')
plt.plot(finance['time'], 0.1*finance['value']+10,label='finance')
plt.plot(game['time'], 1*game['value']+30,label='game')
plt.plot(office['time'], 1*office['value']+40,label='office')
plt.plot(other['time'], 0.1*other['value']+10,label='other')
plt.plot(social['time'], 0.1*social['value'],label='social')
plt.plot(travel['time'], 0.1*travel['value'],label='travel')
plt.plot(unknown['time'], 0.1*unknown['value'],label='unknown')
plt.plot(utilities['time'], utilities['value'],label='utilities')
plt.plot(weather['time'], weather['value'], label='weather')
plt.legend()
plt.ylim([0,100])
plt.show()

### TODO erase data from parients:
# patient 1:    begin ->  14-3-2014  and    16-4-2014 -> end
# patient 2:    begin ->  21-3-2014  and    8-5-2014 -> end
# patient 3:    begin ->  14-3-2014  and    5-5-2014 -> end
# patient 4:    begin ->  24-4-2014  and    8-5-2014 -> end
# patient 5:    begin ->  18-3-2014  and    3-5-2014 -> end
# patient 6:    begin ->  14-3-2014  and    4-5-2014 -> end
# patient 7:    begin ->  21-3-2014  and    27-4-2014 -> end
# patient 8:    begin ->  27-3-2014  and    5-5-2014 -> end
# patient 9:    begin ->  13-3-2014  and    3-5-2014 -> end
# patient 10:   begin ->  21-3-2014  and    5-5-2014 -> end
# patient 11:   begin ->  14-3-2014  and    6-5-2014 -> end
# patient 12:   begin ->  13-3-2014  and    5-5-2014 -> end
# patient 13:   begin ->  20-3-2014  and    5-5-2014 -> end
# patient 14:   begin ->  21-3-2014  and    5-5-2014 -> end
# patient 15:   begin ->  21-3-2014  and    29-4-2014 -> end
# patient 16:   begin ->  22-3-2014  and    4-5-2014 -> end
# patient 17:   begin ->  14-4-2014  and    8-6-2014 -> end
# patient 18:   begin ->  8-4-2014   and    8-5-2014 -> end
# patient 19:   begin ->  12-4-2014  and    29-5-2014 -> end
# patient 20:   begin ->  3-4-2014   and    13-5-2014 -> end
# patient 21:   begin ->  1-4-2014   and    8-5-2014 -> end
# patient 22:   begin ->  2-4-2014   and    13-5-2014 -> end
# patient 23:   begin ->  20-3-2014  and    4-5-2014 -> end
# patient 24:   begin ->  1-4-2014   and    5-5-2014 -> end
# patient 25:   begin ->  1-4-2014   and    13-5-2014 -> end
# patient 26:   begin ->  16-4-2014  and    31-5-2014 -> end

########################################################################################################################

# Explore the mean mood, arousal, ... for a patient: ### TODO the dates are not stored so possibly the plots are not comparable (todo: store date)
patient_data = ('mood','circumplex.arousal' ,'circumplex.valence' ,'activity' ,'screen','call','sms' ,'builtin' ,'communication',
                'entertainment','finance','game','office','other','social','travel','unknown' ,'utilities','weather')

data_patient = {}
for x in patient_data:
    data_patient['mean_' + x] = []

day = None
for i in patient_data:
    patient_data_type = dataset.ix[dataset['id'] == patients[patientnumber]].ix[dataset['variable'] == i]
    value = list()
    new_day = True
    for j, date in enumerate(patient_data_type.time):
        if date.day != day:
            if len(value) > 0:
                data_patient['mean_'+ i].append(np.mean(value))
            else:
                if new_day:
                    data_patient['mean_' + i].append(patient_data_type.iloc[j].value)
                    new_day = False
                # in case no event was on that day
                else:
                    data_patient['mean_' + i].append(0)
            value = list()
            value.append(patient_data_type.iloc[j].value)
        else:
            value.append(patient_data_type.iloc[j].value)
        day = date.day

plt.figure(1)
for x in patient_data:
    m = data_patient['mean_' + x]
    if x != 'mood' and len(data_patient['mean_' + x])>0:
        if x == 'sms':
            m = [y * 5 for y in data_patient['mean_' + x]]
        elif x == 'circumplex.arousal':
            m = [y + 8 for y in data_patient['mean_' + x]]
        elif x == 'circumplex.valence':
            m = [y * 2 for y in data_patient['mean_' + x]]
        elif x == 'call':
            m = [y * 4 for y in data_patient['mean_' + x]]
        else:
            print(x)
            if (np.nanmax(data_patient['mean_' + x])-np.nanmin(data_patient['mean_' + x])) > 0:
                m = [(y / (np.nanmax(data_patient['mean_' + x])-np.nanmin(data_patient['mean_' + x])))*10 for y in data_patient['mean_' + x]]
            else:
                m = [(y / (np.nanmax(data_patient['mean_' + x]))) * 10 for y in data_patient['mean_' + x]]

    plt.plot(m,label= x)
plt.legend()
plt.show()

# compare all events on daytime ### TODO add the morning and evening if statement (see below)(because arousal in the evening seems important)

data_patient_morning = {}
for x in patient_data:
    data_patient_morning['morning_' + x] = []

data_patient_evening = {}
for x in patient_data:
    data_patient_morning['evening_' + x] = []



# Explore How many times a day, a patient scores his/her mood
# mood_per_day = list()
# count_mood = 0
# day = None
# last_mood = 6
# average_mood = list()
# total_mood = list()
# for patient in patients:
#     # patient_data = dataset.ix[dataset['id'] == patient].ix[dataset['variable'] == 'mood']
#     patient_data = dataset.ix[dataset['id'] == patients[14]].ix[dataset['variable'] == 'mood']
#     for i, date in enumerate(patient_data.time):
#         #print(i,date)
#         count_mood += 1
#         average_mood.append(patient_data.iloc[i].value)
#         if date.day != day:
#             mood_per_day.append(last_mood - float(sum(average_mood))/len(average_mood))
#             total_mood.append(float(sum(average_mood)) / len(average_mood))
#             last_mood = float(sum(average_mood))/len(average_mood)
#             average_mood = list()
#         day = date.day
#     print(mood_per_day)
#     #print(range(len(mood_per_day)))
#     plt.plot(range(len(mood_per_day)), mood_per_day)
#     plt.plot(range(len(mood_per_day)), total_mood)
#     plt.show()
#     print(mood_per_day)
#     mood_per_day = list()
#     sys.exit()



########################################################################################################################

#
# print("help")
# print(dataset.ix[dataset['id'] == patients[8]])
# patient_data = dataset.ix[dataset['id'] == patients[14]].ix[dataset['variable'] == 'mood']
# #print(patient_data)
#
# time = dataset.time.unique()

#
# for i, date in enumerate(patient_data.time):
#     while