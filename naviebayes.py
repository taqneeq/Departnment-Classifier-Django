import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pickle
# Load the CSV file with correct delimiter
df = pd.read_csv('Algorithm.csv', delimiter=',')

# Remove columns with 'Unnamed' headers
df = df.loc[:, ~df.columns.str.contains('Unnamed')]

# Use the correct column names
df = df.drop(columns=['Whats your full name?'])

# Define features and target
X = df.drop(columns=['Choose The Department You\'re A Part of ?'])
y = df['Choose The Department You\'re A Part of ?']

# Handle missing values
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize Gaussian Naive Bayes classifier
classifier = GaussianNB()

# Train the classifier using cross-validation
cv_scores = cross_val_score(classifier, X_train_scaled, y_train, cv=5)
print(f'Cross-Validation Scores: {cv_scores}')

# Fit the classifier on the training data
classifier.fit(X_train_scaled, y_train)

# Save the trained model and imputer to a pickle file
with open('naive_bayes_model.pickle', 'wb') as model_file:
    pickle.dump(classifier, model_file)

with open('imputer.pickle', 'wb') as imputer_file:
    pickle.dump(imputer, imputer_file)

# Make predictions on the test set
y_pred = classifier.predict(X_test_scaled)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Test Accuracy: {accuracy:.2f}')

# Now, let's get input values from the user
new_input_values = {}
for feature in X.columns:
    value = input(f'Enter your rating for "{feature}": ')
    new_input_values[feature] = float(value)

# Convert the input values to a DataFrame
new_data = pd.DataFrame([new_input_values])

# Impute missing values in the new data
new_data_imputed = imputer.transform(new_data)

# Standardize the new data
new_data_scaled = scaler.transform(new_data_imputed)

# Make predictions on the new data
predicted_department = classifier.predict(new_data_scaled)

print(f'Predicted Department: {predicted_department[0]}')
