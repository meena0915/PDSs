import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    "Height (inches)": [65.8, 71.5, 69.4, 68.2, 67.8, 68.7, 69.8, 70.1, 67.9, 66.8],
    "Weight (pounds)": [112, 136, 153, 142, 144, 123, 141, 136, 112, 120],
    "Age (years)": [30, 19, 45, 22, 29, 50, 51, 23, 17, 39],
    "Grip strength (kg)": [30, 31, 29, 28, 24, 26, 22, 20, 19, 31],
    "Frailty (Y/N)": ['N', 'N', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Convert frailty to categorical type for better plotting
df['Frailty'] = df['Frailty (Y/N)'].map({'Y': 1, 'N': 0})

# Set the style of seaborn
sns.set(style="whitegrid")

# 1. Grip Strength vs. Frailty
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Grip strength (kg)', y='Frailty', hue='Frailty (Y/N)', style='Frailty (Y/N)', s=100)
plt.title('Grip Strength vs Frailty Status (Scatter Plot)')
plt.xlabel('Grip Strength (kg)')
plt.ylabel('Frailty (Y/N)')
plt.xticks([0, 1], ['N', 'Y'])  # Set x-ticks for frailty
plt.grid(True)
plt.show()

# 2. Grip Strength vs. Height
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Height (inches)', y='Grip strength (kg)', hue='Frailty (Y/N)', style='Frailty (Y/N)', s=100)
plt.title('Grip Strength vs Height')
plt.xlabel('Height (inches)')
plt.ylabel('Grip Strength (kg)')
plt.grid(True)
plt.show()

# 3. Grip Strength vs. Weight
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Weight (pounds)', y='Grip strength (kg)', hue='Frailty (Y/N)', style='Frailty (Y/N)', s=100)
plt.title('Grip Strength vs Weight')
plt.xlabel('Weight (pounds)')
plt.ylabel('Grip Strength (kg)')
plt.grid(True)
plt.show()

# 4. Grip Strength vs. Age
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age (years)', y='Grip strength (kg)', hue='Frailty (Y/N)', style='Frailty (Y/N)', s=100)
plt.title('Grip Strength vs Age')
plt.xlabel('Age (years)')
plt.ylabel('Grip Strength (kg)')
plt.grid(True)
plt.show()

# 5. Box Plot for Grip Strength by Frailty Status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Frailty (Y/N)', y='Grip strength (kg)', data=df, palette="Set2")
plt.title('Grip Strength Distribution by Frailty Status (Box Plot)')
plt.xlabel('Frailty (Y/N)')
plt.ylabel('Grip Strength (kg)')
plt.grid(True)
plt.show()
