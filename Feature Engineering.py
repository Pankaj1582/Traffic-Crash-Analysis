from Datapreprocessing import df
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

# Create a feature for day of the week
df['Day of Week'] = df['Date and Time of Crash'].dt.day_name()

# Create a feature for time of day (Morning, Afternoon, Evening, Night)
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 22:
        return 'Evening'
    else:
        return 'Night'

df['Time of Day'] = df['Hour'].apply(categorize_time_of_day)

# Display the updated DataFrame
print(df.head())


# List of categorical columns to encode
categorical_cols = df.select_dtypes(include='object').columns

# Apply label encoding to each categorical column
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Display the updated DataFrame
print(df.head())

# Columns to scale (numerical columns)
numerical_cols = df.select_dtypes(include=np.number).columns

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the numerical columns
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Display the scaled DataFrame
print(df.head())