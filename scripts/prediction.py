# Predict mood
import numpy as np
import random
from collections import OrderedDict

class PredictMood:
    def __init__(self):
        self.mood_fluctuation_positive = None
        self.mood_fluctuation_negative = None
        self.mood_median_positive = None
        self.mood_median_negative = None
        self.mood_per_day = list()
        self.mood_dict = OrderedDict()
        self.attributes = dict()

    def set_mood_fluctuation(self, positive=None, negative=None, pos_median=None, neg_median=None):
        self.mood_fluctuation_positive = positive
        self.mood_fluctuation_negative = negative
        self.mood_median_positive = pos_median
        self.mood_median_negative = neg_median

    def set_daily_mood(self, mood):
        # For example: {day1: 8, day2: 7}
        previous_day = None
        mood_list = list()
        count_day = 0
        for i, timestamp in enumerate(mood.time):
            current_mood = mood.iloc[i].value
            if not previous_day:
                previous_day = timestamp.day
                mood_list.append(current_mood)
                continue
            if timestamp.day != previous_day:
                count_day += 1
                daily_mood = np.mean(mood_list)
                self.mood_per_day.append(daily_mood)
                self.mood_dict.update({"day_"+str(count_day): daily_mood})
                mood_list = list()
                mood_list.append(current_mood)
            else:
                mood_list.append(current_mood)
            previous_day = timestamp.day

    def predict_next_mood(self):
        for day in self.mood_dict:
            mood = self.mood_dict[day]
            negative_chance = self.mood_fluctuation_positive
            positive_chance = self.mood_fluctuation_negative
            random_value = random.random()
            if random_value <= negative_chance:
                next_mood = mood + self.mood_median_negative
            elif negative_chance < random_value > positive_chance + negative_chance:
                next_mood = mood + self.mood_median_positive
            else:
                next_mood = mood
            try:
                actual_mood = self.mood_dict['day_'+str(int(day.split('_')[1])+1)]
            except KeyError:
                actual_mood = None

            if actual_mood:
                print(next_mood - actual_mood)

    def set_attribute(self, name, values):
        self.attributes.update({name: values})

    def get_attributes(self):
        return self.attributes

    def get_mood_per_day(self):
        return self.mood_per_day

    def get_change(self, attribute_list, change):
        mean = np.mean(attribute_list)
        if change > mean:
            return 'higher'
        elif change < mean:
            return 'lower'
        else:
            return 'same'
