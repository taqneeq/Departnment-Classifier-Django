def get_department(data):

    f = open('random_forest_model.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    # print("hello")

    prediction = classifier.predict(data)
    return prediction

print(get_department(data))