import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/pankajyadav/Desktop/Traffic_Crash/Data/Traffic_crash_dataset.csv')

# Handling wrong values 
df['Date and Time of Crash'] = df['Date and Time of Crash'].replace('17/12/2022', '17/12/2022 00:00')
df['Date and Time of Crash'] = df['Date and Time of Crash'].replace('04/11/2023', '04/11/2023 00:00')

# Convert 'Date and Time of Crash' to datetime
df['Date and Time of Crash'] = pd.to_datetime(df['Date and Time of Crash'], format='%d/%m/%Y %H:%M')

# Extract features like year, month, day, hour
df['Year'] = df['Date and Time of Crash'].dt.year
df['Month'] = df['Date and Time of Crash'].dt.month
df['Day'] = df['Date and Time of Crash'].dt.day
df['Hour'] = df['Date and Time of Crash'].dt.hour

# Display the updated DataFrame
print(df.head())

# Using Label encoding for categorical variables
light_conditions_mapping = {
    'DAYLIGHT': 0,
    'DARK - LIGHTED ROADWAY': 1,
    'DARK - NOT LIGHTED ROADWAY': 2,
    'DUSK': 3,
    'DAWN': 4,
    'UNKNOWN': 5
}
df['Light Conditions Encoded'] = df['Light Conditions'].map(light_conditions_mapping)

# Display value counts for categorical features
print(df['Light Conditions'].value_counts())



