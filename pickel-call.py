# Purpose: To test the random forest model on a random list of length 22
import pandas as pd 
import pickle
import random as rd

# generate a random list of length 22 of integers between 1 and 5
def generate_random_list():
    random_list = []
    for i in range(22):
        random_list.append(rd.randint(1,5))
    return random_list

data = [generate_random_list()]
print(data)
def get_department(data):

    f = open('random_forest_model.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    # print("hello")

    prediction = classifier.predict(data)
    return prediction

print(get_department(data))