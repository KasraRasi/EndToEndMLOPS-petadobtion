# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g9zr5dAT81IX389tBbXoj6z3VtYrp8gA
"""



import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = '/content/pet_adoption_data.csv'
dataset = pd.read_csv(file_path)

# Inspect the data
missing_values = dataset.isnull().sum()
data_types = dataset.dtypes

# Handle missing values (example)
# dataset['ColumnWithMissingValues'].fillna(dataset['ColumnWithMissingValues'].median(), inplace=True)
# dataset.drop(columns=['ColumnWithTooManyMissingValues'], inplace=True)

# Normalize/Standardize numerical features
numerical_features = ['AgeMonths', 'WeightKg', 'AdoptionFee']
scaler = StandardScaler()
dataset[numerical_features] = scaler.fit_transform(dataset[numerical_features])

# Encode categorical features
categorical_features = ['PetType', 'Breed', 'Color', 'Size', 'Vaccinated', 'HealthCondition', 'PreviousOwner']
encoder = OneHotEncoder(sparse=False, drop='first')  # Avoid dummy variable trap
encoded_features = encoder.fit_transform(dataset[categorical_features])

# Create a DataFrame with encoded features
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))

# Drop original categorical columns and concatenate encoded features
dataset = dataset.drop(columns=categorical_features).reset_index(drop=True)
dataset = pd.concat([dataset, encoded_df], axis=1)

# Split the dataset into training and testing sets
X = dataset.drop(columns=['AdoptionLikelihood'])
y = dataset['AdoptionLikelihood']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the first few rows of the preprocessed dataset
X_train.head(), y_train.head()



# Ensure the dataset is updated with the newly created 'ShelterTimeCategory' and 'HealthVaccStatus' features

# Creating Time in Shelter Categories
def shelter_time_category(time_in_shelter_days):
    if time_in_shelter_days <= 30:
        return 'Short'
    elif time_in_shelter_days <= 60:
        return 'Medium'
    else:
        return 'Long'

dataset['ShelterTimeCategory'] = dataset['TimeInShelterDays'].apply(shelter_time_category)

# Creating a combined Health and Vaccination Status
def health_vacc_status(row):
    if row['HealthCondition_1'] == 0 and row['Vaccinated_1'] == 1:
        return 'Healthy and Vaccinated'
    elif row['HealthCondition_1'] == 1 and row['Vaccinated_1'] == 1:
        return 'Sick but Vaccinated'
    elif row['HealthCondition_1'] == 0 and row['Vaccinated_1'] == 0:
        return 'Healthy but Not Vaccinated'
    else:
        return 'Sick and Not Vaccinated'

dataset['HealthVaccStatus'] = dataset.apply(health_vacc_status, axis=1)

# Verify the columns were added
print(dataset.columns)

# Encode newly created categorical features
additional_categorical_features = ['ShelterTimeCategory', 'HealthVaccStatus']
encoder = OneHotEncoder(sparse=False, drop='first')  # Avoid dummy variable trap
encoded_additional_features = encoder.fit_transform(dataset[additional_categorical_features])

# Create a DataFrame with encoded additional features
encoded_additional_df = pd.DataFrame(encoded_additional_features, columns=encoder.get_feature_names_out(additional_categorical_features))

# Drop original additional categorical columns and concatenate encoded features
dataset = dataset.drop(columns=additional_categorical_features).reset_index(drop=True)
dataset = pd.concat([dataset, encoded_additional_df], axis=1)

# Split the updated dataset into training and testing sets again
X = dataset.drop(columns=['AdoptionLikelihood'])
y = dataset['AdoptionLikelihood']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the first few rows of the preprocessed dataset after adding new features
X_train.head(), y_train.head()

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import TensorBoard
import datetime

# Define the model architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Use 'sigmoid' for binary classification
])
# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',  # Use 'binary_crossentropy' for binary classification
              metrics=['accuracy'])

# Setup TensorBoard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

# Train the model
history = model.fit(X_train, y_train,
                    epochs=50,  # Number of epochs
                    batch_size=32,  # Batch size
                    validation_split=0.2,  # Validation split for monitoring validation loss and metrics
                    callbacks=[tensorboard_callback])  # TensorBoard callback

# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)

print(f'Test Loss: {test_loss}')
print(f'Test Accuracy: {test_accuracy}')

!pip install --upgrade imbalanced-learn
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Load the dataset
file_path = '/content/pet_adoption_data.csv'
dataset = pd.read_csv(file_path)

# Inspect the data
missing_values = dataset.isnull().sum()
data_types = dataset.dtypes

# Handle missing values (example)
# dataset['ColumnWithMissingValues'].fillna(dataset['ColumnWithMissingValues'].median(), inplace=True)
# dataset.drop(columns=['ColumnWithTooManyMissingValues'], inplace=True)

# Normalize/Standardize numerical features
numerical_features = ['AgeMonths', 'WeightKg', 'AdoptionFee']
scaler = StandardScaler()
dataset[numerical_features] = scaler.fit_transform(dataset[numerical_features])

# Create additional features
def age_group(age_months):
    if age_months <= 12:
        return 'Puppy/Kitten'
    elif age_months <= 24:
        return 'Young'
    elif age_months <= 96:
        return 'Adult'
    else:
        return 'Senior'

def weight_category(weight_kg):
    if weight_kg < 10:
        return 'Light'
    elif weight_kg <= 20:
        return 'Medium'
    else:
        return 'Heavy'

dataset['AgeGroup'] = dataset['AgeMonths'].apply(age_group)
dataset['WeightCategory'] = dataset['WeightKg'].apply(weight_category)

# Creating Time in Shelter Categories
def shelter_time_category(time_in_shelter_days):
    if time_in_shelter_days <= 30:
        return 'Short'
    elif time_in_shelter_days <= 60:
        return 'Medium'
    else:
        return 'Long'

dataset['ShelterTimeCategory'] = dataset['TimeInShelterDays'].apply(shelter_time_category)

print(dataset.columns)
# Creating a combined Health and Vaccination Status
def health_vacc_status(row):
    if row['HealthCondition'] == 0 and row['Vaccinated'] == 1:
        return 'Healthy and Vaccinated'
    elif row['HealthCondition'] == 1 and row['Vaccinated'] == 1:
        return 'Sick but Vaccinated'
    elif row['HealthCondition'] == 0 and row['Vaccinated'] == 0:
        return 'Healthy but Not Vaccinated'
    else:
        return 'Sick and Not Vaccinated'

dataset['HealthVaccStatus'] = dataset.apply(health_vacc_status, axis=1)

# Encode categorical features
categorical_features = ['PetType', 'Breed', 'Color', 'Size', 'PreviousOwner', 'AgeGroup', 'WeightCategory', 'ShelterTimeCategory', 'HealthVaccStatus']
encoder = OneHotEncoder(sparse=False, drop='first')  # Avoid dummy variable trap
encoded_features = encoder.fit_transform(dataset[categorical_features])

# Create a DataFrame with encoded features
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))

# Drop original categorical columns and concatenate encoded features
dataset = dataset.drop(columns=categorical_features).reset_index(drop=True)
dataset = pd.concat([dataset, encoded_df], axis=1)

# Split the dataset into training and testing sets
X = dataset.drop(columns=['AdoptionLikelihood'])
y = dataset['AdoptionLikelihood']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Handle imbalanced data
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Display the first few rows of the preprocessed dataset after adding new features
X_train_res.head(), y_train_res.head()

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

# Apply SMOTE to training data
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print(f'Resampled dataset shape {y_train_res.value_counts()}')
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import classification_report

# Load the dataset
file_path = '/content/pet_adoption_data.csv'
dataset = pd.read_csv(file_path)

# Inspect the data
missing_values = dataset.isnull().sum()
data_types = dataset.dtypes

# Handle missing values (example)
# dataset['ColumnWithMissingValues'].fillna(dataset['ColumnWithMissingValues'].median(), inplace=True)
# dataset.drop(columns=['ColumnWithTooManyMissingValues'], inplace=True)

# Normalize/Standardize numerical features
numerical_features = ['AgeMonths', 'WeightKg', 'AdoptionFee']
scaler = StandardScaler()
dataset[numerical_features] = scaler.fit_transform(dataset[numerical_features])

# Create additional features
def age_group(age_months):
    if age_months <= 12:
        return 'Puppy/Kitten'
    elif age_months <= 24:
        return 'Young'
    elif age_months <= 96:
        return 'Adult'
    else:
        return 'Senior'

def weight_category(weight_kg):
    if weight_kg < 10:
        return 'Light'
    elif weight_kg <= 20:
        return 'Medium'
    else:
        return 'Heavy'

dataset['AgeGroup'] = dataset['AgeMonths'].apply(age_group)
dataset['WeightCategory'] = dataset['WeightKg'].apply(weight_category)

# Creating Time in Shelter Categories
def shelter_time_category(time_in_shelter_days):
    if time_in_shelter_days <= 30:
        return 'Short'
    elif time_in_shelter_days <= 60:
        return 'Medium'
    else:
        return 'Long'

dataset['ShelterTimeCategory'] = dataset['TimeInShelterDays'].apply(shelter_time_category)

# Creating a combined Health and Vaccination Status
def health_vacc_status(row):
    if row['HealthCondition'] == 0 and row['Vaccinated'] == 1:
        return 'Healthy and Vaccinated'
    elif row['HealthCondition'] == 1 and row['Vaccinated'] == 1:
        return 'Sick but Vaccinated'
    elif row['HealthCondition'] == 0 and row['Vaccinated'] == 0:
        return 'Healthy but Not Vaccinated'
    else:
        return 'Sick and Not Vaccinated'

dataset['HealthVaccStatus'] = dataset.apply(health_vacc_status, axis=1)

# Encode categorical features
categorical_features = ['PetType', 'Breed', 'Color', 'Size', 'PreviousOwner', 'AgeGroup', 'WeightCategory', 'ShelterTimeCategory', 'HealthVaccStatus']
encoder = OneHotEncoder(sparse=False, drop='first')  # Avoid dummy variable trap
encoded_features = encoder.fit_transform(dataset[categorical_features])

# Create a DataFrame with encoded features
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_features))

# Drop original categorical columns and concatenate encoded features
dataset = dataset.drop(columns=categorical_features).reset_index(drop=True)
dataset = pd.concat([dataset, encoded_df], axis=1)

# Split the dataset into training and testing sets
X = dataset.drop(columns=['AdoptionLikelihood'])
y = dataset['AdoptionLikelihood']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to training data
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

print(f'Resampled dataset shape {y_train_res.value_counts()}')

# Build the model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train_res.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

# Compile the model with class weights
class_weights = {0: 1., 1: 3.}  # Adjust the weights based on the class imbalance

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Define callbacks for early stopping and TensorBoard
callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    tf.keras.callbacks.TensorBoard(log_dir='./logs')
]

# Train the model
history = model.fit(X_train_res, y_train_res,
                    validation_split=0.2,
                    epochs=50,
                    batch_size=32,
                    class_weight=class_weights,  # Add class weights here
                    callbacks=callbacks)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_accuracy:.4f}')

# Predict on the test set
y_pred = model.predict(X_test).round()

# Generate a classification report
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import numpy as np

# Train a Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42, class_weight='balanced')
rf_model.fit(X_train_res, y_train_res)

# Predict on the test set with Random Forest
y_pred_rf = rf_model.predict(X_test)
print("Random Forest Classifier Report:")
print(classification_report(y_test, y_pred_rf))

# Cross-validation with Random Forest
cv_scores = cross_val_score(rf_model, X_train_res, y_train_res, cv=5, scoring='accuracy')
print(f'Cross-validation accuracy scores: {cv_scores}')
print(f'Mean cross-validation accuracy: {cv_scores.mean()}')

# Predict on the test set with Keras model
y_pred_nn = model.predict(X_test).round().astype(int)

# Manually average predictions (soft voting)
y_pred_combined = (y_pred_nn + y_pred_rf.reshape(-1, 1)) / 2
y_pred_combined = np.where(y_pred_combined >= 0.5, 1, 0).flatten()

# Generate a combined classification report
print("Combined Model Report:")
print(classification_report(y_test, y_pred_combined))

# Wrap the Keras model in a KerasClassifier for compatibility
!pip install --upgrade --force-reinstall tensorflow
import tensorflow as tf
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

def create_model():
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train_res.shape[1],)),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Create a KerasClassifier instance
nn_classifier = KerasClassifier(build_fn=create_model, epochs=50, batch_size=32, verbose=0)

# Now include this wrapped classifier in the VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('rf', rf_model),
    ('nn', nn_classifier)  # Use the KerasClassifier here
], voting='soft')

voting_clf.fit(X_train_res, y_train_res)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Define the Keras model
def create_keras_model():
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train_res.shape[1],)),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Train the Keras model with different class weights
best_accuracy = 0
best_class_weight = None
for weight in [{0: 1., 1: 2.}, {0: 1., 1: 3.}, {0: 1., 1: 4.}]:
    model = create_keras_model()
    history = model.fit(X_train_res, y_train_res,
                        validation_split=0.2,
                        epochs=50,
                        batch_size=32,
                        class_weight=weight,
                        callbacks=[
                            tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
                            tf.keras.callbacks.TensorBoard(log_dir='./logs')
                        ])
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    if test_accuracy > best_accuracy:
        best_accuracy = test_accuracy
        best_class_weight = weight

print(f'Best Class Weight: {best_class_weight} with Test Accuracy: {best_accuracy:.4f}')

# Train the final Keras model with the best class weight
model = create_keras_model()
history = model.fit(X_train_res, y_train_res,
                    validation_split=0.2,
                    epochs=50,
                    batch_size=32,
                    class_weight=best_class_weight,
                    callbacks=[
                        tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
                        tf.keras.callbacks.TensorBoard(log_dir='./logs')
                    ])

# Predict on the test set with Keras model
y_pred_nn = model.predict(X_test).round().astype(int)

# Hyperparameter tuning for Random Forest
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
rf_model = RandomForestClassifier(random_state=42, class_weight='balanced')
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train_res, y_train_res)
best_rf_model = grid_search.best_estimator_

# Predict on the test set with Random Forest
y_pred_rf = best_rf_model.predict(X_test)
print("Random Forest Classifier Report after tuning:")
print(classification_report(y_test, y_pred_rf))

# Manually average predictions (soft voting)
y_pred_combined = (y_pred_nn + y_pred_rf.reshape(-1, 1)) / 2
y_pred_combined = np.where(y_pred_combined >= 0.5, 1, 0).flatten()

# Generate a combined classification report
print("Combined Model Report:")
print(classification_report(y_test, y_pred_combined))

import joblib

# Save the trained Random Forest model to a file
joblib_file = "random_forest_model.pkl"
joblib.dump(best_rf_model, joblib_file)
print(f"Random Forest model saved to {joblib_file}")

!pip install Flask

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)