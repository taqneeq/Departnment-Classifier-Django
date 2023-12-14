import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import pickle
import random as rd 

df = pd.read_csv('Algorithm.csv', delimiter=',')

df = df.loc[:, ~df.columns.str.contains('Unnamed')]

df = df.drop(columns=['Whats your full name?'])

# Define features and target
X = df.drop(columns=['Choose The Department You\'re A Part of ?'])
y = df['Choose The Department You\'re A Part of ?']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Impute missing values using mean strategy
imputer = SimpleImputer(strategy='mean')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Initialize Random Forest classifier
classifier = RandomForestClassifier(random_state=42)

# Train the classifier using cross-validation
cv_scores = cross_val_score(classifier, X_train_imputed, y_train, cv=5)
print(f'Cross-Validation Scores: {cv_scores}')

# Fit the classifier on the training data
classifier.fit(X_train_imputed, y_train)

# Save the trained model and imputer to a pickle file
with open('random_forest_model.pickle', 'wb') as model_file:
    pickle.dump(classifier, model_file)
# Make predictions on the test set
with open('imputer.pickle', 'wb') as imputer_file:
    pickle.dump(imputer, imputer_file)

# Make predictions on the test set
y_pred = classifier.predict(X_test_imputed)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Test Accuracy: {accuracy:.2f}')

# Now, let's get input values from the user
def generate_random_list():
    random_list = []
    for i in range(22):
        random_list.append(rd.randint(1,5))
    return random_list
new_input_values = generate_random_list();


# Convert the input values to a DataFrame
new_data = pd.DataFrame([new_input_values])

# Impute missing values in the new data
new_data_imputed = imputer.transform(new_data)
print(new_data_imputed)
print(type(new_data_imputed))
# Make predictions on the new data
predicted_department = classifier.predict(new_data_imputed)
string_out = predicted_department[0]
