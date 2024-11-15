import pandas as pd

# Load the raw data
df = pd.read_csv('/content/frailty_project/data_raw/raw_frailty_data.csv')

# Rename the columns to follow the specified format (if needed)
df.columns = ['Height (inches)', 'Weight (pounds)', 'Age (years)', 'Grip strength (kg)', 'Frailty (Y/N)']

# Simple data cleaning, e.g., removing entries with missing values
df_clean = df.dropna()

# Save the cleaned data
df_clean.to_csv('/content/frailty_project/data_clean/cleaned_frailty_data.csv', index=False)



