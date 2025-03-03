import matplotlib.pyplot as plt
import seaborn as sns
from Datapreprocessing import df

# Distribution of crash counts by year
plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=df)
plt.title('Crash Counts by Year')
plt.show()

# Distribution of crashes by light conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='Light Conditions', data=df)
plt.title('Crash Counts by Light Conditions')
plt.xticks(rotation=45)
plt.show()

# Distribution of crashes by weather conditions
plt.figure(figsize=(12, 6))
sns.countplot(x='Weather Conditions', data=df)
plt.title('Crash Counts by Weather Conditions')
plt.xticks(rotation=45)
plt.show()

# Crash counts by light conditions and weather conditions
plt.figure(figsize=(14, 8))
sns.countplot(x='Light Conditions', hue='Weather Conditions', data=df)
plt.title('Crash Counts by Light and Weather Conditions')
plt.xticks(rotation=45)
plt.show()

# Crash counts by road surface and weather conditions
plt.figure(figsize=(14, 8))
sns.countplot(x='Road Surface', hue='Weather Conditions', data=df)
plt.title('Crash Counts by Road Surface and Weather Conditions')
plt.xticks(rotation=45)
plt.show()

# Correlation matrix
correlation_matrix = df.corr()

# Heatmap of the correlation matrix
plt.figure(figsize=(20, 18))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
