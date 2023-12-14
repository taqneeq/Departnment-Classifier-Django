import pickle
import os 
import pandas as pd
from django.conf import settings

def get_department(data):
    pickle_file_path = os.path.join(settings.STATIC_ROOT, "website/data.pickle")
    f = open(pickle_file_path, 'rb')
    classifier = pickle.load(f)
    f.close()
    # print("hello")
    sample = {
    'I can make friends easily': [data[0]],
    'I possess good communication skills': [data[1]],
    'I am good at art and designs': [data[2]],
    'I am good at programming and have sound technical skills': [data[3]],
    'I am good at convincing people': [data[4]],
    'I am good at innovation and ideation': [data[5]],
    'I am good at problem solving': [data[6]],
    'I am good at thinking of creative games': [data[7]],
    'I enjoy building corporate relations': [data[8]],
    'I am good at negotiating & bargaining': [data[9]],
    'I enjoy doing hospitality': [data[10]],
    'I tend to keep up with the latest social media trends': [data[11]],
    'I am good at organising and managing': [data[12]],
    'I drive to college': [data[13]],
    'I can understand composition, rhythm and quality of social media posts': [data[14]],
    'I am good at sketching out my creative ideas': [data[15]],
    'I tend to keep up with the latest tech trends': [data[16]],
    "I'm good at managing finances": [data[17]],
    'I am good with words and content writing': [data[18]],
    'I am good at thinking of tech-based events': [data[19]],
    'I am good at taking photos and videos': [data[20]],
    'I have good relations with people from other MPSTME committees': [data[21]]
    }
    sample = pd.DataFrame.from_dict(sample)

    prediction = classifier.predict(sample) if prediction else "Unknown"
    return prediction[0].upper()