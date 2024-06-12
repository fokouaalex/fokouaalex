import pandas as pd

# Load the Excel file
file_path = 'JEOPARDY_CSV.xlsx'  # Update with your file path
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Strip any leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# Check for missing values
print(df.isnull().sum())

# Handle missing values (if any)
df.dropna(inplace=True)  # Drop rows with any missing values