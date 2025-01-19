# # inspect_pickle.py

# import pickle

# # Load the saved model and feature names
# with open("random_forest_model.pkl", 'rb') as f:
#     content = pickle.load(f)

# print(type(content))
# if isinstance(content, tuple):
#     print(f"Tuple length: {len(content)}")
#     for item in content:
#         print(type(item))
# else:
#     print("Content is not a tuple")
import pandas as pd
import joblib
import pickle

# Load the model and feature names
with open("random_forest_model.pkl", 'rb') as f:
    model, feature_names = pickle.load(f)

# Sample input data
sample_data = {
    "PetID": [1],
    "PetType": ["Cat"],
    "Breed": ["Persian"],
    "AgeMonths": [24],
    "Color": ["Brown"],
    "Size": ["Small"],
    "WeightKg": [5.5],
    "Vaccinated": [1],
    "HealthCondition": [0],
    "TimeInShelterDays": [20],
    "AdoptionFee": [100],
    "PreviousOwner": [0]
}

# Convert to DataFrame
df = pd.DataFrame(sample_data)

# Apply the same preprocessing steps
df['AgeGroup'] = df['AgeMonths'].apply(lambda age_months: 'Puppy/Kitten' if age_months <= 12 else 'Young' if age_months <= 24 else 'Adult' if age_months <= 96 else 'Senior')
df['WeightCategory'] = df['WeightKg'].apply(lambda weight_kg: 'Light' if weight_kg < 10 else 'Medium' if weight_kg <= 20 else 'Heavy')
df['ShelterTimeCategory'] = df['TimeInShelterDays'].apply(lambda days: 'Short' if days <= 30 else 'Medium' if days <= 60 else 'Long')
df['HealthVaccStatus'] = df.apply(lambda row: 'Healthy and Vaccinated' if row['HealthCondition'] == 0 and row['Vaccinated'] == 1 else 'Sick but Vaccinated' if row['HealthCondition'] == 1 and row['Vaccinated'] == 1 else 'Healthy but Not Vaccinated' if row['HealthCondition'] == 0 and row['Vaccinated'] == 0 else 'Sick and Not Vaccinated', axis=1)

# Encoding categorical features
df = pd.get_dummies(df, columns=['PetType', 'Breed', 'Color', 'Size', 'PreviousOwner', 'AgeGroup', 'WeightCategory', 'ShelterTimeCategory', 'HealthVaccStatus'], drop_first=True)

# Align dataframe with model input
missing_cols = set(feature_names) - set(df.columns)
for col in missing_cols:
    df[col] = 0
df = df[feature_names]

# Make predictions
predictions = model.predict(df)
print(predictions)
